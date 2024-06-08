import argparse
import os
import sys
from pathlib import Path
from one_click import *


check_env()

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--update-wizard', action='store_true', help='Launch a menu with update options.')
args, _ = parser.parse_known_args()


if not is_installed():
    install_webui()
    os.chdir(script_dir)

if os.environ.get("LAUNCH_AFTER_INSTALL", "").lower() in ("no", "n", "false", "0", "f", "off"):
    print_big_message("Will now exit due to LAUNCH_AFTER_INSTALL.")
    sys.exit()
    
# Workaround for llama-cpp-python loading paths in CUDA env vars even if they do not exist
conda_path_bin = os.path.join(conda_env_path, "bin")
if not os.path.exists(conda_path_bin):
    os.mkdir(conda_path_bin)    

# ABUS - start Kara
print("Start the program...")
run_cmd(f"python start-kara.py", environment=True) 
    
