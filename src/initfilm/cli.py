import typer, initfilm
from . import main, config, transcode



app = typer.Typer(add_completion=False)
app.add_typer(config.app, name="config", help="Manage configuration settings.")
def cli():
    app()



@app.callback(invoke_without_command=True)
def default(context: typer.Context):
    if context.invoked_subcommand is None: # Only run if no subcommand is provided
        main.createFolder_level0()

@app.command()
def create_proxies(folder_footage:str, codec: str = 'h264', resolution: str = '1280x720'):
    """Create proxies for footage in the specified footage folder."""
    transcode.transcode_footage(folder_footage, codec, resolution)

@app.command()
def version():
    """Print the current version."""
    version = initfilm.__version__
    print(version)