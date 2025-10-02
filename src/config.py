from enum import Enum
import urllib

import os
from typing import List
from urllib.parse import urlparse
import json5
import torch

from tqdm import tqdm

import structlog
logger = structlog.get_logger()

class UserConfig:
    def __init__(self, user_config_path):
        self.user_config_path = user_config_path
        self.default_user_config = {
            "asr_engine": "faster-whisper",
            "gradio_language": "Korean",
            "whisper_model": "large",
            "faster_whisper_model": "large",
            "whisper_timestamped_model": "large",
            "whisperX_model": "large",            
            "whisper_language": "korean",
            "word_timestamps": True,
            "denoise": False,
            "burn_subtitles": False,
            "video_quality": "best",
            "audio_format": "flac",
            "demucs_model": "htdemucs",
            "karaoke_mode": "Instrumental",
            "pitch_change": 0,
            "pitch_change_all": 0,
            "index_rate": 0.5,
            "filter_radius": 3,
            "rms_mix_rate": 0.25,
            "protect": 0.33,
            "main_vocal_gain": 0,
            "backup_vocal_gain": 0,
            "inst_gain": 0,
            "reverb_rm_size": 0.15,
            "reverb_wet": 0.2,
            "reverb_dry": 0.8,
            "reverb_damping": 0.7,
            "demixing_model": "htdemucs",
            "demixing_audio_format": "flac",
            "translate_source_language": "English",
            "translate_target_language": "korean",
            "denoise_level" : 0,
            "whisper_compute_type" : 'default',
            "whisper_highlight_words" : False,
            "last_folder" : ".",     
            "xtts_language": "Korean",                                
            "xtts_voice": "",
            "xtts_rate": 1,
            "xtts_volume": 1,
            "xtts_pitch": 0,
            "ms_language": "English",
            "ms_voice": "UNITED STATES-Ana-Female",
            "azure_tts_pitch": 0,
            "azure_tts_rate": 0,
            "azure_tts_volume": 0,
            "edge_tts_pitch": 0,
            "edge_tts_rate": 0,
            "edge_tts_volume": 0,            
            "f5_single_language": "English",
            "f5_multi_language1": "English",
            "f5_multi_language2": "English",            
            "cosy_voice_language": "English",
            "kokoro_language": "American English",
            "rvc_voice": "choi",
            "rvc_f0_up_key": 0,
            "rvc_filter_radius": 3,
            "rvc_index_rate": 0.3,
            "rvc_rms_mix_rate": 1,
            "rvc_protect": 0.23,
            "rvc_hop_length": 256,
            "rvc_clean_strength": 0.2,   
            "var_enable": False,
            "var_mode": 0,
            "vsr_enable": True,
            "vsr_mode": 0,
            "vsr_scale": 2,
            "compression_enable": True,
            "compression_crf": 23,
            "compression_preset": "medium"            
            }
        self.user_config = self.load_user_config()


    def load_user_config(self):
        try:
            with open(self.user_config_path, "r", encoding='utf-8') as file:
                return json5.load(file)
        except Exception as e:
            logger.error(f"[config.py] load_user_config - Error transcribing file: {e}")
            return self.default_user_config

    def save_user_config(self):
        with open(self.user_config_path, "w", encoding='utf-8') as file:
            json5.dump(self.user_config, file, indent=4)

    def get(self, key, default=None):
        value = self.user_config.get(key, default)
        if value != None:
            return value
        else:
            return self.default_user_config.get(key, key)

    def set(self, key, value):
        self.user_config[key] = value
        self.save_user_config()


