from datetime import datetime
import json
import math
from typing import Iterator, Union

from io import StringIO
import os
import pathlib
import tempfile
import zipfile
import numpy as np

import torch
import gradio as gr
import ffmpeg


from src.config import VAD_INITIAL_PROMPT_MODE_VALUES, ApplicationConfig, VadInitialPromptMode
from src.hooks.progressListener import ProgressListener
from src.hooks.subTaskProgressListener import SubTaskProgressListener
from src.hooks.whisperProgressHook import create_progress_listener_handle

from src.modelCache import ModelCache
from src.prompts.jsonPromptStrategy import JsonPromptStrategy
from src.prompts.prependPromptStrategy import PrependPromptStrategy
from src.source import get_audio_source_collection
from src.vadParallel import ParallelContext, ParallelTranscription

from src.download import ExceededMaximumDuration, download_url
from src.utils import optional_int, slugify, write_srt, write_vtt
from src.vad import AbstractTranscription, NonSpeechStrategy, PeriodicTranscriptionConfig, TranscriptionConfig, VadPeriodicTranscription, VadSileroTranscription
from src.container.abstractWhisperContainer import AbstractWhisperContainer
from src.container.whisperFactory import create_whisper_container


# Environment
script_dir = os.getcwd()
whisper_temp_path = os.path.join(script_dir, "installer_files", "gradio")

# Configure more application defaults in config.json5

# Gradio seems to truncate files without keeping the extension, so we need to truncate the file prefix ourself 
MAX_FILE_PREFIX_LENGTH = 17

# Limit auto_parallel to a certain number of CPUs (specify vad_cpu_cores to get a higher number)
MAX_AUTO_CPU_CORES = 8

WHISPER_MODELS = ["tiny", "base", "small", "medium", "large-v1", "large-v2"]

class VadOptions:
    def __init__(self, vad: str = None, vadMergeWindow: float = 5, vadMaxMergeSize: float = 150, vadPadding: float = 1, vadPromptWindow: float = 1, 
                                        vadInitialPromptMode: Union[VadInitialPromptMode, str] = VadInitialPromptMode.PREPREND_FIRST_SEGMENT):
        self.vad = vad
        self.vadMergeWindow = vadMergeWindow
        self.vadMaxMergeSize = vadMaxMergeSize
        self.vadPadding = vadPadding
        self.vadPromptWindow = vadPromptWindow
        self.vadInitialPromptMode = vadInitialPromptMode if isinstance(vadInitialPromptMode, VadInitialPromptMode) \
                                        else VadInitialPromptMode.from_string(vadInitialPromptMode)

class WhisperTranscriber:
    def __init__(self, input_audio_max_duration: float = None, vad_process_timeout: float = None, 
                 vad_cpu_cores: int = 1, delete_uploaded_files: bool = False, output_dir: str = None, 
                 app_config: ApplicationConfig = None):
        self.model_cache = ModelCache()
        self.parallel_device_list = None
        self.gpu_parallel_context = None
        self.cpu_parallel_context = None
        self.vad_process_timeout = vad_process_timeout
        self.vad_cpu_cores = vad_cpu_cores

        self.vad_model = None
        self.inputAudioMaxDuration = input_audio_max_duration
        self.deleteUploadedFiles = delete_uploaded_files
        self.output_dir = output_dir

        self.app_config = app_config

    def set_parallel_devices(self, vad_parallel_devices: str):
        self.parallel_device_list = [ device.strip() for device in vad_parallel_devices.split(",") ] if vad_parallel_devices else None

    def set_auto_parallel(self, auto_parallel: bool):
        if auto_parallel:
            if torch.cuda.is_available():
                self.parallel_device_list = [ str(gpu_id) for gpu_id in range(torch.cuda.device_count())]

            self.vad_cpu_cores = min(os.cpu_count(), MAX_AUTO_CPU_CORES)
            print("[Auto parallel] Using GPU devices " + str(self.parallel_device_list) + " and " + str(self.vad_cpu_cores) + " CPU cores for VAD/transcription.")

    # Entry function for the simple tab
    def transcribe_webui_simple(self, modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                                vad, vadMergeWindow, vadMaxMergeSize, 
                                word_timestamps: bool = False, highlight_words: bool = False):
        return self.transcribe_webui_simple_progress(modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                                                     vad, vadMergeWindow, vadMaxMergeSize, 
                                                     word_timestamps, highlight_words)
    
    # Entry function for the simple tab progress
    def transcribe_webui_simple_progress(self, modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                                         vad, vadMergeWindow, vadMaxMergeSize, 
                                         word_timestamps: bool = False, highlight_words: bool = False, 
                                         progress=gr.Progress()):
        
        vadOptions = VadOptions(vad, vadMergeWindow, vadMaxMergeSize, self.app_config.vad_padding, self.app_config.vad_prompt_window, self.app_config.vad_initial_prompt_mode)

        return self.transcribe_webui(modelName, languageName, urlData, multipleFiles, microphoneData, task, vadOptions, 
                                     word_timestamps=word_timestamps, highlight_words=highlight_words, progress=progress)

    # Entry function for the full tab
    def transcribe_webui_full(self, modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                              vad, vadMergeWindow, vadMaxMergeSize, vadPadding, vadPromptWindow, vadInitialPromptMode, 
                              # Word timestamps
                              word_timestamps: bool, highlight_words: bool, prepend_punctuations: str, append_punctuations: str,
                              initial_prompt: str, temperature: float, best_of: int, beam_size: int, patience: float, length_penalty: float, suppress_tokens: str, 
                              condition_on_previous_text: bool, fp16: bool, temperature_increment_on_fallback: float, 
                              compression_ratio_threshold: float, logprob_threshold: float, no_speech_threshold: float):
        
        return self.transcribe_webui_full_progress(modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                                vad, vadMergeWindow, vadMaxMergeSize, vadPadding, vadPromptWindow, vadInitialPromptMode,
                                word_timestamps, highlight_words, prepend_punctuations, append_punctuations,
                                initial_prompt, temperature, best_of, beam_size, patience, length_penalty, suppress_tokens,
                                condition_on_previous_text, fp16, temperature_increment_on_fallback,
                                compression_ratio_threshold, logprob_threshold, no_speech_threshold)

    # Entry function for the full tab with progress
    def transcribe_webui_full_progress(self, modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                                        vad, vadMergeWindow, vadMaxMergeSize, vadPadding, vadPromptWindow, vadInitialPromptMode,
                                        # Word timestamps
                                        word_timestamps: bool, highlight_words: bool, prepend_punctuations: str, append_punctuations: str,   
                                        initial_prompt: str, temperature: float, best_of: int, beam_size: int, patience: float, length_penalty: float, suppress_tokens: str, 
                                        condition_on_previous_text: bool, fp16: bool, temperature_increment_on_fallback: float, 
                                        compression_ratio_threshold: float, logprob_threshold: float, no_speech_threshold: float, 
                                        progress=gr.Progress()):

        # Handle temperature_increment_on_fallback
        if temperature_increment_on_fallback is not None:
            temperature = tuple(np.arange(temperature, 1.0 + 1e-6, temperature_increment_on_fallback))
        else:
            temperature = [temperature]

        vadOptions = VadOptions(vad, vadMergeWindow, vadMaxMergeSize, vadPadding, vadPromptWindow, vadInitialPromptMode)

        return self.transcribe_webui(modelName, languageName, urlData, multipleFiles, microphoneData, task, vadOptions,
                                     initial_prompt=initial_prompt, temperature=temperature, best_of=best_of, beam_size=beam_size, patience=patience, length_penalty=length_penalty, suppress_tokens=suppress_tokens,
                                     condition_on_previous_text=condition_on_previous_text, fp16=fp16,
                                     compression_ratio_threshold=compression_ratio_threshold, logprob_threshold=logprob_threshold, no_speech_threshold=no_speech_threshold, 
                                     word_timestamps=word_timestamps, prepend_punctuations=prepend_punctuations, append_punctuations=append_punctuations, highlight_words=highlight_words,
                                     progress=progress)

    def transcribe_webui(self, modelName, languageName, urlData, multipleFiles, microphoneData, task, 
                         vadOptions: VadOptions, progress: gr.Progress = None, highlight_words: bool = False, 
                         **decodeOptions: dict):
        try:
            sources = self.__get_source(urlData, multipleFiles, microphoneData)

            try:
                selectedLanguage = languageName.lower() if len(languageName) > 0 else None
                selectedModel = modelName if modelName is not None else "base"

                model = create_whisper_container(whisper_implementation=self.app_config.whisper_implementation, 
                                                 model_name=selectedModel, compute_type=self.app_config.compute_type, 
                                                 cache=self.model_cache, models=self.app_config.models)

                # Result
                download = []
                zip_file_lookup = {}
                text = ""
                vtt = ""

                # Write result
                downloadDirectory = tempfile.mkdtemp(dir=whisper_temp_path)
                source_index = 0

                outputDirectory = self.output_dir if self.output_dir is not None else downloadDirectory

                # Progress
                total_duration = sum([source.get_audio_duration() for source in sources])
                current_progress = 0

                # A listener that will report progress to Gradio
                root_progress_listener = self._create_progress_listener(progress, "Transcribe")

                # Execute whisper
                for source in sources:
                    source_prefix = ""
                    source_audio_duration = source.get_audio_duration()

                    if (len(sources) > 1):
                        # Prefix (minimum 2 digits)
                        source_index += 1
                        source_prefix = str(source_index).zfill(2) + "_"
                        print("Transcribing ", source.source_path)

                    scaled_progress_listener = SubTaskProgressListener(root_progress_listener, 
                                                   base_task_total=total_duration,
                                                   sub_task_start=current_progress,
                                                   sub_task_total=source_audio_duration)

                    # Transcribe
                    result = self.transcribe_file(model, source.source_path, selectedLanguage, task, vadOptions, scaled_progress_listener, **decodeOptions)
                    # filePrefix = slugify(source_prefix + source.get_short_name(), allow_unicode=True)
                    filePrefix = source_prefix + source.get_file_name()

                    # Update progress
                    current_progress += source_audio_duration

                    source_download, source_text, source_vtt = self.write_result(result, filePrefix, outputDirectory, highlight_words)

                    if len(sources) > 1:
                        # Add new line separators
                        if (len(source_text) > 0):
                            source_text += os.linesep + os.linesep
                        if (len(source_vtt) > 0):
                            source_vtt += os.linesep + os.linesep

                        # Append file name to source text too
                        source_text = source.get_full_name() + ":" + os.linesep + source_text
                        source_vtt = source.get_full_name() + ":" + os.linesep + source_vtt

                    # Add to result
                    download.extend(source_download)
                    text += source_text
                    vtt += source_vtt

                    if (len(sources) > 1):
                        # Zip files support at least 260 characters, but we'll play it safe and use 200
                        zipFilePrefix = slugify(source_prefix + source.get_short_name(max_length=200), allow_unicode=True)

                        # File names in ZIP file can be longer
                        for source_download_file in source_download:
                            # Get file postfix (after last -)
                            filePostfix = os.path.basename(source_download_file).split("-")[-1]
                            zip_file_name = zipFilePrefix + "-" + filePostfix
                            zip_file_lookup[source_download_file] = zip_file_name

                # Create zip file from all sources
                if len(sources) > 1:
                    downloadAllPath = os.path.join(downloadDirectory, "All_Output-" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".zip")

                    with zipfile.ZipFile(downloadAllPath, 'w', zipfile.ZIP_DEFLATED) as zip:
                        for download_file in download:
                            # Get file name from lookup
                            zip_file_name = zip_file_lookup.get(download_file, os.path.basename(download_file))
                            zip.write(download_file, arcname=zip_file_name)

                    download.insert(0, downloadAllPath)

                return download, text, vtt

            finally:
                # Cleanup source
                if self.deleteUploadedFiles:
                    for source in sources:
                        print("Deleting source file " + source.source_path)

                        try:
                            os.remove(source.source_path)
                        except Exception as e:
                            # Ignore error - it's just a cleanup
                            print("Error deleting source file " + source.source_path + ": " + str(e))
        
        except ExceededMaximumDuration as e:
            return [], ("[ERROR]: Maximum remote video length is " + str(e.maxDuration) + "s, file was " + str(e.videoDuration) + "s"), "[ERROR]"

    def transcribe_file(self, model: AbstractWhisperContainer, audio_path: str, language: str, task: str = None, 
                        vadOptions: VadOptions = VadOptions(), 
                        progressListener: ProgressListener = None, **decodeOptions: dict):
        
        initial_prompt = decodeOptions.pop('initial_prompt', None)

        if progressListener is None:
            # Default progress listener
            progressListener = ProgressListener()

        if ('task' in decodeOptions):
            task = decodeOptions.pop('task')

        initial_prompt_mode = vadOptions.vadInitialPromptMode

        # Set default initial prompt mode
        if (initial_prompt_mode is None):
            initial_prompt_mode = VadInitialPromptMode.PREPREND_FIRST_SEGMENT

        if (initial_prompt_mode == VadInitialPromptMode.PREPEND_ALL_SEGMENTS or 
            initial_prompt_mode == VadInitialPromptMode.PREPREND_FIRST_SEGMENT):
            # Prepend initial prompt
            prompt_strategy = PrependPromptStrategy(initial_prompt, initial_prompt_mode)
        elif (vadOptions.vadInitialPromptMode == VadInitialPromptMode.JSON_PROMPT_MODE):
            # Use a JSON format to specify the prompt for each segment
            prompt_strategy = JsonPromptStrategy(initial_prompt)
        else:
            raise ValueError("Invalid vadInitialPromptMode: " + initial_prompt_mode)

        # Callable for processing an audio file
        whisperCallable = model.create_callback(language, task, prompt_strategy=prompt_strategy, **decodeOptions)

        # The results
        if (vadOptions.vad == 'silero-vad'):
            # Silero VAD where non-speech gaps are transcribed
            process_gaps = self._create_silero_config(NonSpeechStrategy.CREATE_SEGMENT, vadOptions)
            result = self.process_vad(audio_path, whisperCallable, self.vad_model, process_gaps, progressListener=progressListener)
        elif (vadOptions.vad == 'silero-vad-skip-gaps'):
            # Silero VAD where non-speech gaps are simply ignored
            skip_gaps = self._create_silero_config(NonSpeechStrategy.SKIP, vadOptions)
            result = self.process_vad(audio_path, whisperCallable, self.vad_model, skip_gaps, progressListener=progressListener)
        elif (vadOptions.vad == 'silero-vad-expand-into-gaps'):
            # Use Silero VAD where speech-segments are expanded into non-speech gaps
            expand_gaps = self._create_silero_config(NonSpeechStrategy.EXPAND_SEGMENT, vadOptions)
            result = self.process_vad(audio_path, whisperCallable, self.vad_model, expand_gaps, progressListener=progressListener)
        elif (vadOptions.vad == 'periodic-vad'):
            # Very simple VAD - mark every 5 minutes as speech. This makes it less likely that Whisper enters an infinite loop, but
            # it may create a break in the middle of a sentence, causing some artifacts.
            periodic_vad = VadPeriodicTranscription()
            period_config = PeriodicTranscriptionConfig(periodic_duration=vadOptions.vadMaxMergeSize, max_prompt_window=vadOptions.vadPromptWindow)
            result = self.process_vad(audio_path, whisperCallable, periodic_vad, period_config, progressListener=progressListener)

        else:
            if (self._has_parallel_devices()):
                # Use a simple period transcription instead, as we need to use the parallel context
                periodic_vad = VadPeriodicTranscription()
                period_config = PeriodicTranscriptionConfig(periodic_duration=math.inf, max_prompt_window=1)

                result = self.process_vad(audio_path, whisperCallable, periodic_vad, period_config, progressListener=progressListener)
            else:
                # Default VAD
                result = whisperCallable.invoke(audio_path, 0, None, None, progress_listener=progressListener)

        return result

    def _create_progress_listener(self, progress: gr.Progress, desc: str = ""):
        if (progress is None):
            # Dummy progress listener
            return ProgressListener()
        
        class ForwardingProgressListener(ProgressListener):
            def __init__(self, progress: gr.Progress):
                self.progress = progress

            def on_progress(self, current: Union[int, float], total: Union[int, float]):
                # From 0 to 1
                self.progress(current / total, desc)

            def on_finished(self):
                self.progress(1, desc)

        return ForwardingProgressListener(progress)

    def process_vad(self, audio_path, whisperCallable, vadModel: AbstractTranscription, vadConfig: TranscriptionConfig, 
                    progressListener: ProgressListener = None):
        if (not self._has_parallel_devices()):
            # No parallel devices, so just run the VAD and Whisper in sequence
            return vadModel.transcribe(audio_path, whisperCallable, vadConfig, progressListener=progressListener)

        gpu_devices = self.parallel_device_list

        if (gpu_devices is None or len(gpu_devices) == 0):
            # No GPU devices specified, pass the current environment variable to the first GPU process. This may be NULL.
            gpu_devices = [os.environ.get("CUDA_VISIBLE_DEVICES", None)]

        # Create parallel context if needed
        if (self.gpu_parallel_context is None):
            # Create a context wih processes and automatically clear the pool after 1 hour of inactivity
            self.gpu_parallel_context = ParallelContext(num_processes=len(gpu_devices), auto_cleanup_timeout_seconds=self.vad_process_timeout)
        # We also need a CPU context for the VAD
        if (self.cpu_parallel_context is None):
            self.cpu_parallel_context = ParallelContext(num_processes=self.vad_cpu_cores, auto_cleanup_timeout_seconds=self.vad_process_timeout)

        parallel_vad = ParallelTranscription()
        return parallel_vad.transcribe_parallel(transcription=vadModel, audio=audio_path, whisperCallable=whisperCallable,  
                                                config=vadConfig, cpu_device_count=self.vad_cpu_cores, gpu_devices=gpu_devices, 
                                                cpu_parallel_context=self.cpu_parallel_context, gpu_parallel_context=self.gpu_parallel_context, 
                                                progress_listener=progressListener) 

    def _has_parallel_devices(self):
        return (self.parallel_device_list is not None and len(self.parallel_device_list) > 0) or self.vad_cpu_cores > 1

    def _concat_prompt(self, prompt1, prompt2):
        if (prompt1 is None):
            return prompt2
        elif (prompt2 is None):
            return prompt1
        else:
            return prompt1 + " " + prompt2

    def _create_silero_config(self, non_speech_strategy: NonSpeechStrategy, vadOptions: VadOptions):
        # Use Silero VAD 
        if (self.vad_model is None):
            self.vad_model = VadSileroTranscription()

        config = TranscriptionConfig(non_speech_strategy = non_speech_strategy, 
                max_silent_period=vadOptions.vadMergeWindow, max_merge_size=vadOptions.vadMaxMergeSize, 
                segment_padding_left=vadOptions.vadPadding, segment_padding_right=vadOptions.vadPadding, 
                max_prompt_window=vadOptions.vadPromptWindow)

        return config

    def write_result(self, result: dict, source_name: str, output_dir: str, highlight_words: bool = False):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        text = result["text"]
        language = result["language"]
        languageMaxLineWidth = self.__get_max_line_width(language)

        print("Max line width " + str(languageMaxLineWidth))
        vtt = self.__get_subs(result["segments"], "vtt", languageMaxLineWidth, highlight_words=highlight_words)
        srt = self.__get_subs(result["segments"], "srt", languageMaxLineWidth, highlight_words=highlight_words)
        json_result = json.dumps(result, indent=4, ensure_ascii=False)

        output_files = []
        output_files.append(self.__create_file(srt, output_dir, source_name + ".srt"));
        output_files.append(self.__create_file(vtt, output_dir, source_name + ".vtt"));
        output_files.append(self.__create_file(text, output_dir, source_name + ".txt"));
        output_files.append(self.__create_file(json_result, output_dir, source_name + ".json"));

        # output_files.append(self.__create_file(srt, output_dir, source_name + "_(" + language + ").srt"));
        # output_files.append(self.__create_file(vtt, output_dir, source_name + "_(" + language + ").vtt"));
        # output_files.append(self.__create_file(text, output_dir, source_name + "_(" + language + ").txt"));
        # output_files.append(self.__create_file(json_result, output_dir, source_name + "_(" + language + ").json"));

        return output_files, text, vtt

    def clear_cache(self):
        self.model_cache.clear()
        self.vad_model = None

    def __get_source(self, urlData, multipleFiles, microphoneData):
        return get_audio_source_collection(urlData, multipleFiles, microphoneData, self.inputAudioMaxDuration)

    def __get_max_line_width(self, language: str) -> int:
        if (language and language.lower() in ["japanese", "ja", "chinese", "zh", "korean", "ko"]):
            # Chinese characters and kana are wider, so limit line length to 40 characters
            return 30
        else:
            # TODO: Add more languages
            # 80 latin characters should fit on a 1080p/720p screen
            return 60

    def __get_subs(self, segments: Iterator[dict], format: str, maxLineWidth: int, highlight_words: bool = False) -> str:
        segmentStream = StringIO()

        if format == 'vtt':
            write_vtt(segments, file=segmentStream, maxLineWidth=maxLineWidth, highlight_words=highlight_words)
        elif format == 'srt':
            write_srt(segments, file=segmentStream, maxLineWidth=maxLineWidth, highlight_words=highlight_words)
        else:
            raise Exception("Unknown format " + format)

        segmentStream.seek(0)
        return segmentStream.read()

    def __create_file(self, text: str, directory: str, fileName: str) -> str:
        # Write the text to a file
        with open(os.path.join(directory, fileName), 'w+', encoding="utf-8") as file:
            file.write(text)

        return file.name

    def close(self):
        print("Closing parallel contexts")
        self.clear_cache()

        if (self.gpu_parallel_context is not None):
            self.gpu_parallel_context.close()
        if (self.cpu_parallel_context is not None):
            self.cpu_parallel_context.close()