import json
from configparser import ConfigParser

import typer
from pathlib import Path

APP_NAME = "bing-img-search"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
config_path = app_dir / "config.cfg"

config = ConfigParser()
config.read(config_path)


def check_config():
    """
    check if api key set
    :return: Bing Image Search api key
    """
    if not config_path.is_file():
        typer.echo("Bing image search api key not set")
        raise typer.Exit()

    # with open(config_path) as file:
    #     config_data = json.load(file)
    #     BING_API_KEY = config_data["bing_api"]
    config.read(config_path)
    BING_API_KEY = config.get('main', 'bing_api')

    if BING_API_KEY:
        return BING_API_KEY
    if not BING_API_KEY:
        typer.echo("bing image search api key not set, set it using bing-img-search set-api-key")
        raise typer.Exit()
