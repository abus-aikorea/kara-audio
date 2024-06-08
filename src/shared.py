import argparse
import copy
import os
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

# from src.logging_colors import logger
import structlog
logger = structlog.get_logger()

# Model variables
model = None
tokenizer = None
model_name = 'None'
is_seq2seq = False
model_dirty_from_training = False
lora_names = []

# Generation variables
stop_everything = False
generation_lock = None
processing_message = '*Is typing...*'

# UI variables
gradio = {}
persistent_interface_state = {}
need_restart = False

# UI defaults
settings = {
    'dark_theme': True,
    'show_controls': True,
    'start_with': '',
    'mode': 'chat',
    'chat_style': 'cai-chat',
    'prompt-default': 'QA',
    'prompt-notebook': 'QA',
    'preset': 'simple-1',
    'max_new_tokens': 512,
    'max_new_tokens_min': 1,
    'max_new_tokens_max': 4096,
    'negative_prompt': '',
    'seed': -1,
    'truncation_length': 2048,
    'truncation_length_min': 0,
    'truncation_length_max': 200000,
    'max_tokens_second': 0,
    'max_updates_second': 0,
    'prompt_lookup_num_tokens': 0,
    'custom_stopping_strings': '',
    'custom_token_bans': '',
    'auto_max_new_tokens': False,
    'ban_eos_token': False,
    'add_bos_token': True,
    'skip_special_tokens': True,
    'stream': True,
    'character': 'Assistant',
    'name1': 'You',
    'user_bio': '',
    'custom_system_message': '',
    'instruction_template_str': "{%- set ns = namespace(found=false) -%}\n{%- for message in messages -%}\n    {%- if message['role'] == 'system' -%}\n        {%- set ns.found = true -%}\n    {%- endif -%}\n{%- endfor -%}\n{%- if not ns.found -%}\n    {{- '' + 'Below is an instruction that describes a task. Write a response that appropriately completes the request.' + '\\n\\n' -}}\n{%- endif %}\n{%- for message in messages %}\n    {%- if message['role'] == 'system' -%}\n        {{- '' + message['content'] + '\\n\\n' -}}\n    {%- else -%}\n        {%- if message['role'] == 'user' -%}\n            {{-'### Instruction:\\n' + message['content'] + '\\n\\n'-}}\n        {%- else -%}\n            {{-'### Response:\\n' + message['content'] + '\\n\\n' -}}\n        {%- endif -%}\n    {%- endif -%}\n{%- endfor -%}\n{%- if add_generation_prompt -%}\n    {{-'### Response:\\n'-}}\n{%- endif -%}",
    'chat_template_str': "{%- for message in messages %}\n    {%- if message['role'] == 'system' -%}\n        {%- if message['content'] -%}\n            {{- message['content'] + '\\n\\n' -}}\n        {%- endif -%}\n        {%- if user_bio -%}\n            {{- user_bio + '\\n\\n' -}}\n        {%- endif -%}\n    {%- else -%}\n        {%- if message['role'] == 'user' -%}\n            {{- name1 + ': ' + message['content'] + '\\n'-}}\n        {%- else -%}\n            {{- name2 + ': ' + message['content'] + '\\n' -}}\n        {%- endif -%}\n    {%- endif -%}\n{%- endfor -%}",
    'chat-instruct_command': 'Continue the chat dialogue below. Write a single reply for the character "<|character|>".\n\n<|prompt|>',
    'autoload_model': False,
    'gallery-items_per_page': 50,
    'gallery-open': False,
    'default_extensions': ['gallery'],
}

default_settings = copy.deepcopy(settings)

# Parser copied from https://github.com/vladmandic/automatic
parser = argparse.ArgumentParser(description="Text generation web UI", conflict_handler='resolve', add_help=True, formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=55, indent_increment=2, width=200))

# Basic settings
group = parser.add_argument_group('Basic settings')
group.add_argument('--multi-user', action='store_true', help='Multi-user mode. Chat histories are not saved or automatically loaded. Warning: this is likely not safe for sharing publicly.')
group.add_argument('--character', type=str, help='The name of the character to load in chat mode by default.')
group.add_argument('--model', type=str, help='Name of the model to load by default.')
group.add_argument('--lora', type=str, nargs='+', help='The list of LoRAs to load. If you want to load more than one LoRA, write the names separated by spaces.')
group.add_argument('--model-dir', type=str, default='models/', help='Path to directory with all the models.')
group.add_argument('--lora-dir', type=str, default='loras/', help='Path to directory with all the loras.')
group.add_argument('--model-menu', action='store_true', help='Show a model menu in the terminal when the web UI is first launched.')
group.add_argument('--settings', type=str, help='Load the default interface settings from this yaml file. See settings-template.yaml for an example. If you create a file called settings.yaml, this file will be loaded by default without the need to use the --settings flag.')
group.add_argument('--extensions', type=str, nargs='+', help='The list of extensions to load. If you want to load more than one extension, write the names separated by spaces.')
group.add_argument('--verbose', action='store_true', help='Print the prompts to the terminal.')
group.add_argument('--chat-buttons', action='store_true', help='Show buttons on the chat tab instead of a hover menu.')

# Model loader
group = parser.add_argument_group('Model loader')
group.add_argument('--loader', type=str, help='Choose the model loader manually, otherwise, it will get autodetected. Valid options: Transformers, llama.cpp, llamacpp_HF, ExLlamav2_HF, ExLlamav2, AutoGPTQ, AutoAWQ, GPTQ-for-LLaMa, ctransformers, QuIP#.')

# Transformers/Accelerate
group = parser.add_argument_group('Transformers/Accelerate')
group.add_argument('--cpu', action='store_true', help='Use the CPU to generate text. Warning: Training on CPU is extremely slow.')
group.add_argument('--auto-devices', action='store_true', help='Automatically split the model across the available GPU(s) and CPU.')
group.add_argument('--gpu-memory', type=str, nargs='+', help='Maximum GPU memory in GiB to be allocated per GPU. Example: --gpu-memory 10 for a single GPU, --gpu-memory 10 5 for two GPUs. You can also set values in MiB like --gpu-memory 3500MiB.')
group.add_argument('--cpu-memory', type=str, help='Maximum CPU memory in GiB to allocate for offloaded weights. Same as above.')
group.add_argument('--disk', action='store_true', help='If the model is too large for your GPU(s) and CPU combined, send the remaining layers to the disk.')
group.add_argument('--disk-cache-dir', type=str, default='cache', help='Directory to save the disk cache to. Defaults to "cache".')
group.add_argument('--load-in-8bit', action='store_true', help='Load the model with 8-bit precision (using bitsandbytes).')
group.add_argument('--bf16', action='store_true', help='Load the model with bfloat16 precision. Requires NVIDIA Ampere GPU.')
group.add_argument('--no-cache', action='store_true', help='Set use_cache to False while generating text. This reduces VRAM usage slightly, but it comes at a performance cost.')
group.add_argument('--trust-remote-code', action='store_true', help='Set trust_remote_code=True while loading the model. Necessary for some models.')
group.add_argument('--force-safetensors', action='store_true', help='Set use_safetensors=True while loading the model. This prevents arbitrary code execution.')
group.add_argument('--no_use_fast', action='store_true', help='Set use_fast=False while loading the tokenizer (it\'s True by default). Use this if you have any problems related to use_fast.')
group.add_argument('--use_flash_attention_2', action='store_true', help='Set use_flash_attention_2=True while loading the model.')

# bitsandbytes 4-bit
group = parser.add_argument_group('bitsandbytes 4-bit')
group.add_argument('--load-in-4bit', action='store_true', help='Load the model with 4-bit precision (using bitsandbytes).')
group.add_argument('--use_double_quant', action='store_true', help='use_double_quant for 4-bit.')
group.add_argument('--compute_dtype', type=str, default='float16', help='compute dtype for 4-bit. Valid options: bfloat16, float16, float32.')
group.add_argument('--quant_type', type=str, default='nf4', help='quant_type for 4-bit. Valid options: nf4, fp4.')

# llama.cpp
group = parser.add_argument_group('llama.cpp')
group.add_argument('--tensorcores', action='store_true', help='Use llama-cpp-python compiled with tensor cores support. This increases performance on RTX cards. NVIDIA only.')
group.add_argument('--n_ctx', type=int, default=2048, help='Size of the prompt context.')
group.add_argument('--threads', type=int, default=0, help='Number of threads to use.')
group.add_argument('--threads-batch', type=int, default=0, help='Number of threads to use for batches/prompt processing.')
group.add_argument('--no_mul_mat_q', action='store_true', help='Disable the mulmat kernels.')
group.add_argument('--n_batch', type=int, default=512, help='Maximum number of prompt tokens to batch together when calling llama_eval.')
group.add_argument('--no-mmap', action='store_true', help='Prevent mmap from being used.')
group.add_argument('--mlock', action='store_true', help='Force the system to keep the model in RAM.')
group.add_argument('--n-gpu-layers', type=int, default=0, help='Number of layers to offload to the GPU.')
group.add_argument('--tensor_split', type=str, default=None, help='Split the model across multiple GPUs. Comma-separated list of proportions. Example: 18,17.')
group.add_argument('--numa', action='store_true', help='Activate NUMA task allocation for llama.cpp.')
group.add_argument('--logits_all', action='store_true', help='Needs to be set for perplexity evaluation to work. Otherwise, ignore it, as it makes prompt processing slower.')
group.add_argument('--no_offload_kqv', action='store_true', help='Do not offload the  K, Q, V to the GPU. This saves VRAM but reduces the performance.')
group.add_argument('--cache-capacity', type=str, help='Maximum cache capacity (llama-cpp-python). Examples: 2000MiB, 2GiB. When provided without units, bytes will be assumed.')
group.add_argument('--row_split', action='store_true', help='Split the model by rows across GPUs. This may improve multi-gpu performance.')
group.add_argument('--streaming-llm', action='store_true', help='Activate StreamingLLM to avoid re-evaluating the entire prompt when old messages are removed.')
group.add_argument('--attention-sink-size', type=int, default=5, help='StreamingLLM: number of sink tokens. Only used if the trimmed prompt does not share a prefix with the old prompt.')

# ExLlamaV2
group = parser.add_argument_group('ExLlamaV2')
group.add_argument('--gpu-split', type=str, help='Comma-separated list of VRAM (in GB) to use per GPU device for model layers. Example: 20,7,7.')
group.add_argument('--autosplit', action='store_true', help='Autosplit the model tensors across the available GPUs. This causes --gpu-split to be ignored.')
group.add_argument('--max_seq_len', type=int, default=2048, help='Maximum sequence length.')
group.add_argument('--cfg-cache', action='store_true', help='ExLlamav2_HF: Create an additional cache for CFG negative prompts. Necessary to use CFG with that loader.')
group.add_argument('--no_flash_attn', action='store_true', help='Force flash-attention to not be used.')
group.add_argument('--cache_8bit', action='store_true', help='Use 8-bit cache to save VRAM.')
group.add_argument('--cache_4bit', action='store_true', help='Use Q4 cache to save VRAM.')
group.add_argument('--num_experts_per_token', type=int, default=2, help='Number of experts to use for generation. Applies to MoE models like Mixtral.')

# AutoGPTQ
group = parser.add_argument_group('AutoGPTQ')
group.add_argument('--triton', action='store_true', help='Use triton.')
group.add_argument('--no_inject_fused_attention', action='store_true', help='Disable the use of fused attention, which will use less VRAM at the cost of slower inference.')
group.add_argument('--no_inject_fused_mlp', action='store_true', help='Triton mode only: disable the use of fused MLP, which will use less VRAM at the cost of slower inference.')
group.add_argument('--no_use_cuda_fp16', action='store_true', help='This can make models faster on some systems.')
group.add_argument('--desc_act', action='store_true', help='For models that do not have a quantize_config.json, this parameter is used to define whether to set desc_act or not in BaseQuantizeConfig.')
group.add_argument('--disable_exllama', action='store_true', help='Disable ExLlama kernel, which can improve inference speed on some systems.')
group.add_argument('--disable_exllamav2', action='store_true', help='Disable ExLlamav2 kernel.')

# GPTQ-for-LLaMa
group = parser.add_argument_group('GPTQ-for-LLaMa')
group.add_argument('--wbits', type=int, default=0, help='Load a pre-quantized model with specified precision in bits. 2, 3, 4 and 8 are supported.')
group.add_argument('--model_type', type=str, help='Model type of pre-quantized model. Currently LLaMA, OPT, and GPT-J are supported.')
group.add_argument('--groupsize', type=int, default=-1, help='Group size.')
group.add_argument('--pre_layer', type=int, nargs='+', help='The number of layers to allocate to the GPU. Setting this parameter enables CPU offloading for 4-bit models. For multi-gpu, write the numbers separated by spaces, eg --pre_layer 30 60.')
group.add_argument('--checkpoint', type=str, help='The path to the quantized checkpoint file. If not specified, it will be automatically detected.')
group.add_argument('--monkey-patch', action='store_true', help='Apply the monkey patch for using LoRAs with quantized models.')

# HQQ
group = parser.add_argument_group('HQQ')
group.add_argument('--hqq-backend', type=str, default='PYTORCH_COMPILE', help='Backend for the HQQ loader. Valid options: PYTORCH, PYTORCH_COMPILE, ATEN.')

# DeepSpeed
group = parser.add_argument_group('DeepSpeed')
group.add_argument('--deepspeed', action='store_true', help='Enable the use of DeepSpeed ZeRO-3 for inference via the Transformers integration.')
group.add_argument('--nvme-offload-dir', type=str, help='DeepSpeed: Directory to use for ZeRO-3 NVME offloading.')
group.add_argument('--local_rank', type=int, default=0, help='DeepSpeed: Optional argument for distributed setups.')

# RoPE
group = parser.add_argument_group('RoPE')
group.add_argument('--alpha_value', type=float, default=1, help='Positional embeddings alpha factor for NTK RoPE scaling. Use either this or compress_pos_emb, not both.')
group.add_argument('--rope_freq_base', type=int, default=0, help='If greater than 0, will be used instead of alpha_value. Those two are related by rope_freq_base = 10000 * alpha_value ^ (64 / 63).')
group.add_argument('--compress_pos_emb', type=int, default=1, help="Positional embeddings compression factor. Should be set to (context length) / (model\'s original context length). Equal to 1/rope_freq_scale.")

# Gradio
group = parser.add_argument_group('Gradio')
group.add_argument('--listen', action='store_true', help='Make the web UI reachable from your local network.')
group.add_argument('--listen-port', type=int, help='The listening port that the server will use.')
group.add_argument('--listen-host', type=str, help='The hostname that the server will use.')
group.add_argument('--share', action='store_true', help='Create a public URL. This is useful for running the web UI on Google Colab or similar.')
group.add_argument('--auto-launch', action='store_true', default=False, help='Open the web UI in the default browser upon launch.')
group.add_argument('--gradio-auth', type=str, help='Set Gradio authentication password in the format "username:password". Multiple credentials can also be supplied with "u1:p1,u2:p2,u3:p3".', default=None)
group.add_argument('--gradio-auth-path', type=str, help='Set the Gradio authentication file path. The file should contain one or more user:password pairs in the same format as above.', default=None)
group.add_argument('--ssl-keyfile', type=str, help='The path to the SSL certificate key file.', default=None)
group.add_argument('--ssl-certfile', type=str, help='The path to the SSL certificate cert file.', default=None)

# API
group = parser.add_argument_group('API')
group.add_argument('--api', action='store_true', help='Enable the API extension.')
group.add_argument('--public-api', action='store_true', help='Create a public URL for the API using Cloudfare.')
group.add_argument('--public-api-id', type=str, help='Tunnel ID for named Cloudflare Tunnel. Use together with public-api option.', default=None)
group.add_argument('--api-port', type=int, default=5000, help='The listening port for the API.')
group.add_argument('--api-key', type=str, default='', help='API authentication key.')
group.add_argument('--admin-key', type=str, default='', help='API authentication key for admin tasks like loading and unloading models. If not set, will be the same as --api-key.')
group.add_argument('--nowebui', action='store_true', help='Do not launch the Gradio UI. Useful for launching the API in standalone mode.')

# Multimodal
group = parser.add_argument_group('Multimodal')
group.add_argument('--multimodal-pipeline', type=str, default=None, help='The multimodal pipeline to use. Examples: llava-7b, llava-13b.')

# Deprecated parameters
# group = parser.add_argument_group('Deprecated')

args = parser.parse_args()
args_defaults = parser.parse_args([])
provided_arguments = []
for arg in sys.argv[1:]:
    arg = arg.lstrip('-').replace('-', '_')
    if hasattr(args, arg):
        provided_arguments.append(arg)

deprecated_args = []


def do_cmd_flags_warnings():

    # Deprecation warnings
    for k in deprecated_args:
        if getattr(args, k):
            logger.warning(f'The --{k} flag has been deprecated and will be removed soon. Please remove that flag.')

    # Security warnings
    if args.trust_remote_code:
        logger.warning('trust_remote_code is enabled. This is dangerous.')
    if 'COLAB_GPU' not in os.environ and not args.nowebui:
        if args.share:
            logger.warning("The gradio \"share link\" feature uses a proprietary executable to create a reverse tunnel. Use it with care.")
        if any((args.listen, args.share)) and not any((args.gradio_auth, args.gradio_auth_path)):
            logger.warning("\nYou are potentially exposing the web UI to the entire internet without any access password.\nYou can create one with the \"--gradio-auth\" flag like this:\n\n--gradio-auth username:password\n\nMake sure to replace username:password with your own.")
            if args.multi_user:
                logger.warning('\nThe multi-user mode is highly experimental and should not be shared publicly.')


def fix_loader_name(name):
    if not name:
        return name

    name = name.lower()
    if name in ['llamacpp', 'llama.cpp', 'llama-cpp', 'llama cpp']:
        return 'llama.cpp'
    if name in ['llamacpp_hf', 'llama.cpp_hf', 'llama-cpp-hf', 'llamacpp-hf', 'llama.cpp-hf']:
        return 'llamacpp_HF'
    elif name in ['transformers', 'huggingface', 'hf', 'hugging_face', 'hugging face']:
        return 'Transformers'
    elif name in ['autogptq', 'auto-gptq', 'auto_gptq', 'auto gptq']:
        return 'AutoGPTQ'
    elif name in ['gptq-for-llama', 'gptqforllama', 'gptqllama', 'gptq for llama', 'gptq_for_llama']:
        return 'GPTQ-for-LLaMa'
    elif name in ['exllama', 'ex-llama', 'ex_llama', 'exlama']:
        return 'ExLlama'
    elif name in ['exllamav2', 'exllama-v2', 'ex_llama-v2', 'exlamav2', 'exlama-v2', 'exllama2', 'exllama-2']:
        return 'ExLlamav2'
    elif name in ['exllamav2-hf', 'exllamav2_hf', 'exllama-v2-hf', 'exllama_v2_hf', 'exllama-v2_hf', 'exllama2-hf', 'exllama2_hf', 'exllama-2-hf', 'exllama_2_hf', 'exllama-2_hf']:
        return 'ExLlamav2_HF'
    elif name in ['ctransformers', 'ctranforemrs', 'ctransformer']:
        return 'ctransformers'
    elif name in ['autoawq', 'awq', 'auto-awq']:
        return 'AutoAWQ'
    elif name in ['quip#', 'quip-sharp', 'quipsharp', 'quip_sharp']:
        return 'QuIP#'
    elif name in ['hqq']:
        return 'HQQ'


def add_extension(name, last=False):
    if args.extensions is None:
        args.extensions = [name]
    elif last:
        args.extensions = [x for x in args.extensions if x != name]
        args.extensions.append(name)
    elif name not in args.extensions:
        args.extensions.append(name)


def is_chat():
    return True


def load_user_config():
    '''
    Loads custom model-specific settings
    '''
    if Path(f'{args.model_dir}/config-user.yaml').exists():
        file_content = open(f'{args.model_dir}/config-user.yaml', 'r').read().strip()

        if file_content:
            user_config = yaml.safe_load(file_content)
        else:
            user_config = {}
    else:
        user_config = {}

    return user_config


args.loader = fix_loader_name(args.loader)

# Activate the multimodal extension
if args.multimodal_pipeline is not None:
    add_extension('multimodal')

# Activate the API extension
if args.api or args.public_api:
    add_extension('openai', last=True)

# Load model-specific settings
with Path(f'{args.model_dir}/config.yaml') as p:
    if p.exists():
        model_config = yaml.safe_load(open(p, 'r').read())
    else:
        model_config = {}

# Load custom model-specific settings
user_config = load_user_config()

model_config = OrderedDict(model_config)
user_config = OrderedDict(user_config)
