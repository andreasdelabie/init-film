import typer, initfilm
from typing_extensions import Annotated
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
def create_proxies(
    folder_footage:Annotated[str, typer.Option(help='Full path to footage folder.')],
    codec:Annotated[str, typer.Option(help="Use 'h264', 'dnxhr', 'prores-proxy' or 'prores-lt'")]=config.get('proxies', 'default_codec'),
    resolution:Annotated[str, typer.Option(help="Ex. '1280x720', '1920x1080', '3840x2160'")]=config.get('proxies', 'default_resolution')):
    """Create proxies for footage in the specified footage folder."""
    transcode.transcode_footage(folder_footage, codec, resolution)

@app.command()
def version():
    """Print the current version."""
    version = initfilm.__version__
    print(version)