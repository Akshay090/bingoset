import typer
from pathlib import Path

from bingoset.utilities.config import read_config

APP_NAME = "bing-img-search"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
config_path = app_dir / "config.cfg"


def check_config():
    """
    check if api key set
    :return: Bing Image Search api key
    """
    if not config_path.is_file():
        typer.echo("Bing image search api key not set")
        raise typer.Exit()

    BING_API_KEY = read_config('main', 'bing_api', 'str')

    if BING_API_KEY:
        return BING_API_KEY
    if not BING_API_KEY:
        typer.echo("bing image search api key not set, set it using bing-img-search set-api-key")
        raise typer.Exit()
