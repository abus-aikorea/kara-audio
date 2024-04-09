import abc
from typing import Any, Callable, List

from src.config import ModelConfig, VadInitialPromptMode

from src.hooks.progressListener import ProgressListener
from src.modelCache import GLOBAL_MODEL_CACHE, ModelCache
from src.prompts.abstractPromptStrategy import AbstractPromptStrategy

class AbstractWhisperCallback:
    def __init__(self):
        pass

    @abc.abstractmethod
    def invoke(self, audio, segment_index: int, prompt: str, detected_language: str, progress_listener: ProgressListener = None):
        """
        Peform the transcription of the given audio file or data.

        Parameters
        ----------
        audio: Union[str, np.ndarray, torch.Tensor]
            The audio file to transcribe, or the audio data as a numpy array or torch tensor.
        segment_index: int
            The target language of the transcription. If not specified, the language will be inferred from the audio content.
        task: str
            The task - either translate or transcribe.
        progress_listener: ProgressListener
            A callback to receive progress updates.
        """
        raise NotImplementedError()

class LambdaWhisperCallback(AbstractWhisperCallback):
    def __init__(self, callback_lambda: Callable[[Any, int, str, str, ProgressListener], None]):
        super().__init__()
        self.callback_lambda = callback_lambda

    def invoke(self, audio, segment_index: int, prompt: str, detected_language: str, progress_listener: ProgressListener = None):
        return self.callback_lambda(audio, segment_index, prompt, detected_language, progress_listener)

class AbstractWhisperContainer:
    def __init__(self, model_name: str, device: str = None, compute_type: str = "float16",
                 download_root: str = None,
                 cache: ModelCache = None, models: List[ModelConfig] = []):
        self.model_name = model_name
        self.device = device
        self.compute_type = compute_type
        self.download_root = download_root
        self.cache = cache

        # Will be created on demand
        self.model = None

        # List of known models
        self.models = models
    
    def get_model(self):
        if self.model is None:

            if (self.cache is None):
                self.model = self._create_model()
            else:
                model_key = "WhisperContainer." + self.model_name + ":" + (self.device if self.device else '')
                self.model = self.cache.get(model_key, self._create_model)
        return self.model
    
    @abc.abstractmethod
    def _create_model(self):
        raise NotImplementedError()

    def ensure_downloaded(self):
        pass

    @abc.abstractmethod
    def create_callback(self, language: str = None, task: str = None, 
                        prompt_strategy: AbstractPromptStrategy = None, 
                        **decodeOptions: dict) -> AbstractWhisperCallback:
        """
        Create a WhisperCallback object that can be used to transcript audio files.

        Parameters
        ----------
        language: str
            The target language of the transcription. If not specified, the language will be inferred from the audio content.
        task: str
            The task - either translate or transcribe.
        prompt_strategy: AbstractPromptStrategy
            The prompt strategy to use for the transcription.
        decodeOptions: dict
            Additional options to pass to the decoder. Must be pickleable.

        Returns
        -------
        A WhisperCallback object.
        """
        raise NotImplementedError()

    # This is required for multiprocessing
    def __getstate__(self):
        return { 
            "model_name": self.model_name, 
            "device": self.device, 
            "download_root": self.download_root, 
            "models": self.models, 
            "compute_type": self.compute_type 
        }

    def __setstate__(self, state):
        self.model_name = state["model_name"]
        self.device = state["device"]
        self.download_root = state["download_root"]
        self.models = state["models"]
        self.compute_type = state["compute_type"]
        self.model = None
        # Depickled objects must use the global cache
        self.cache = GLOBAL_MODEL_CACHE