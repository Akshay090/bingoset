import json
from pathlib import Path
from configparser import ConfigParser

import typer
import os

from bingoset.search_bing_api import get_images_bing

APP_NAME = "bing-img-search"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
app_dir.mkdir(parents=True, exist_ok=True)
config_path = app_dir / "config.cfg"

app = typer.Typer()
config = ConfigParser()


def write_config():
    config_file = open(config_path, 'w')
    config.write(config_file)
    config_file.close()


if not os.path.exists(config_path):
    config['main'] = {'MAX_RESULTS': '250', 'GROUP_SIZE': '50'}
    write_config()


@app.callback()
def callback():
    """
    Build image dataset using bing image search api
    """


@app.command()
def set_api_key(api_key: str):
    """
      Set Bing Image Search API key
      """
    config.read(config_path)
    config.set('main', 'bing_api', api_key)
    write_config()


@app.command()
def set_max_results(max_number: int):
    """
      Set Max Image number : Default is 250
      """
    config.read(config_path)
    config.set('main', 'max_results', max_number)
    write_config()


@app.command()
def set_group_size(group_size: str):
    """
      Set Group size : default 50
      """
    config.read(config_path)
    config.set('main', 'group_size', group_size)
    write_config()


@app.command()
def q(query: str):
    """
      Search query to search Bing Image API for
      """
    config.read(config_path)
    MAX_RESULTS = config.getint('main', 'max_results')
    GROUP_SIZE = config.getint('main', 'group_size')
    get_images_bing(query, MAX_RESULTS, GROUP_SIZE)
