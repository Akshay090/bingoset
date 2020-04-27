import typer
from pathlib import Path
from configparser import ConfigParser
import os

config = ConfigParser()


APP_NAME = "bing-img-search"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
app_dir.mkdir(parents=True, exist_ok=True)
config_path = app_dir / "config.cfg"


def write_config_file():
    config_file = open(config_path, 'w')
    config.write(config_file)
    config_file.close()


# Initialize Default Config
def initialize_config():
    if not os.path.exists(config_path):
        config['main'] = {'MAX_RESULTS': '250', 'GROUP_SIZE': '50', 'BASE_FOLDER_NAME': 'dataset'}
        write_config_file()


def write_config(section, key, value):
    config.read(config_path)
    config.set(section, key, value)
    write_config_file()


def read_config(section, key, return_type):
    config.read(config_path)
    if return_type == 'int':
        return config.getint(section, key)
    elif return_type == 'str':
        return config.get(section, key)

