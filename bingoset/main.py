import typer
from bingoset.search_bing_api import get_images_bing
from bingoset.utilities.checks import check_config
from bingoset.utilities.config import write_config, read_config, initialize_config

app = typer.Typer()

initialize_config()


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
    write_config('main', 'bing_api', api_key)


@app.command()
def set_max_results(max_number: int):
    """
      Set Max images per request : Default is 250
      """
    write_config('main', 'max_results', max_number)


@app.command()
def set_group_size(group_size: str):
    """
      Set Group size : default 50
      """
    write_config('main', 'group_size', group_size)


@app.command()
def set_base_folder_name(folder_name: str):
    """
      Set Base folder name : default dataset
      """
    write_config('main', 'BASE_FOLDER_NAME', folder_name)


@app.command()
def q(query: str):
    """
      Search query to search Bing Image API for
      """
    API_KEY = check_config()
    MAX_RESULTS = read_config('main', 'max_results', 'int')
    GROUP_SIZE = read_config('main', 'group_size', 'int')
    BASE_FOLDER_NAME = read_config('main', 'BASE_FOLDER_NAME', 'str')
    get_images_bing(query, API_KEY, MAX_RESULTS, GROUP_SIZE, BASE_FOLDER_NAME)
