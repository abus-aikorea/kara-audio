import json
from typing import Dict
from src.prompts.abstractPromptStrategy import AbstractPromptStrategy


class JsonPromptSegment():
    def __init__(self, segment_index: int, prompt: str, format_prompt: bool = False):
        self.prompt = prompt
        self.segment_index = segment_index
        self.format_prompt = format_prompt

class JsonPromptStrategy(AbstractPromptStrategy):
    def __init__(self, initial_json_prompt: str):
        """
        Parameters
        ----------
            initial_json_prompt: str
                The initial prompts for each segment in JSON form.

                Format:
                [
                    {"segment_index": 0, "prompt": "Hello, how are you?"},
                    {"segment_index": 1, "prompt": "I'm doing well, how are you?"},
                    {"segment_index": 2, "prompt": "{0} Fine, thank you.", "format_prompt": true}
                ]
                    
        """
        parsed_json = json.loads(initial_json_prompt)
        self.segment_lookup: Dict[str, JsonPromptSegment] = dict() 
        
        for prompt_entry in parsed_json:
            segment_index = prompt_entry["segment_index"]
            prompt = prompt_entry["prompt"]
            format_prompt = prompt_entry.get("format_prompt", False)
            self.segment_lookup[str(segment_index)] = JsonPromptSegment(segment_index, prompt, format_prompt)

    def get_segment_prompt(self, segment_index: int, whisper_prompt: str, detected_language: str) -> str:
        # Lookup prompt
        prompt = self.segment_lookup.get(str(segment_index), None)

        if (prompt is None):
            # No prompt found, return whisper prompt
            print(f"Could not find prompt for segment {segment_index}, returning whisper prompt")
            return whisper_prompt

        if (prompt.format_prompt):
            return prompt.prompt.format(whisper_prompt)
        else:
            return self._concat_prompt(prompt.prompt, whisper_prompt)
