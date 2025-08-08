import typer, importlib.metadata
from . import main, shortcut, config, templates, transcode



app = typer.Typer(add_completion=False)
def cli():
    app()


@app.callback(invoke_without_command=True)
def default(context: typer.Context):
    if context.invoked_subcommand is None: # Only run if no subcommand is provided
        main.createFolder_level0()

@app.command()
def create_proxies(folder_footage:str, codec: str = 'h264', resolution: str = '1280x720'):
    transcode.transcode_folder(folder_footage, codec, resolution)

@app.command()
def set_prefix(visibility: str):
    """Set prefix visibility to 'visible' or 'hidden'."""
    config.setPrefixVisibility(visibility)

@app.command()
def set_number_style(style: str):
    """Set number style to 'default' or 'double'."""
    config.setNumberStyle(style)

@app.command()
def set_separator_style(style: str):
    """Set separator style to 'dot', 'underscore', 'parenthesis' or 'space'."""
    config.setSeparatorStyle(style)

@app.command()
def set_templates_path(path: str):
    """Set templates path (source path) to 'python' or custom path. ALWAYS USE FORWARD SLASHES!"""
    config.set("templates", "path", path)

@app.command()
def show_templates_path():
    """Print the current templates path."""
    print(templates.template_path)

@app.command()
def show_config():
    """Print the current configuration."""
    config.show()

@app.command()
def add_shortcut():
    """Adds the Init-Film shortcut to the Windows context menu (right click menu)."""
    shortcut.add()

@app.command()
def remove_shortcut():
    """Removes the Init-Film shortcut from the Windows context menu (right click menu)."""
    shortcut.remove()

@app.command()
def version():
    """Print the current version."""
    version = importlib.metadata.version("init-film")
    print(version)