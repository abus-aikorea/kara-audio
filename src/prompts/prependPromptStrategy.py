from src.config import VadInitialPromptMode
from src.prompts.abstractPromptStrategy import AbstractPromptStrategy

class PrependPromptStrategy(AbstractPromptStrategy):
    """
    A simple prompt strategy that prepends a single prompt to all segments of audio, or prepends the prompt to the first segment of audio.
    """
    def __init__(self, initial_prompt: str, initial_prompt_mode: VadInitialPromptMode):
        """
        Parameters
        ----------
            initial_prompt: str
                The initial prompt to use for the transcription.
            initial_prompt_mode: VadInitialPromptMode
                The mode to use for the initial prompt. If set to PREPEND_FIRST_SEGMENT, the initial prompt will be prepended to the first segment of audio.
                If set to PREPEND_ALL_SEGMENTS, the initial prompt will be prepended to all segments of audio.
        """
        self.initial_prompt = initial_prompt
        self.initial_prompt_mode = initial_prompt_mode

        # This is a simple prompt strategy, so we only support these two modes
        if initial_prompt_mode not in [VadInitialPromptMode.PREPEND_ALL_SEGMENTS, VadInitialPromptMode.PREPREND_FIRST_SEGMENT]:
            raise ValueError(f"Unsupported initial prompt mode {initial_prompt_mode}")

    def get_segment_prompt(self, segment_index: int, whisper_prompt: str, detected_language: str) -> str:
        if (self.initial_prompt_mode == VadInitialPromptMode.PREPEND_ALL_SEGMENTS):
            return self._concat_prompt(self.initial_prompt, whisper_prompt)
        elif (self.initial_prompt_mode == VadInitialPromptMode.PREPREND_FIRST_SEGMENT):
            return self._concat_prompt(self.initial_prompt, whisper_prompt) if segment_index == 0 else whisper_prompt
        else:
            raise ValueError(f"Unknown initial prompt mode {self.initial_prompt_mode}")