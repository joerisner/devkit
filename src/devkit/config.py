import os
import sys
from pathlib import Path

import yaml

from .utils import error, out


def get_config_file_path():
    if os.getenv('DEVKIT_CONFIG_FILE'):
        return Path(os.getenv('DEVKIT_CONFIG_FILE'))

    return Path.home() / '.config' / 'devkit' / 'config.yml'


CONFIG_FILE = get_config_file_path()


def load_config():
    try:
        with open(CONFIG_FILE) as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        error('No config file found')
        out("\nSet DEVKIT_CONFIG_FILE or create a new config file at '$HOME/.config/devkit/config.yml'.")
        sys.exit(1)
