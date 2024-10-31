import json 
import os

config_file = os.path.expanduser(os.path.join("~", "Nova", "config.json"))

def load_config():
    with open(config_file) as f:
        config = json.load(f)
        return config["config"]