# Copyright (C) 2025  Andreas Delabie

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



import typer, initfilm
from typing_extensions import Annotated
from . import main, config, transcode, ffmpeg_installscript, license



app = typer.Typer(add_completion=False, context_settings={'help_option_names': ['--help', '-h']})
app.add_typer(license.app, name='license', help='Show license information.')
app.add_typer(config.app, name='config', help='Manage configuration settings.')
def cli():
    app()



@app.callback(invoke_without_command=True)
def default(context: typer.Context):
    if context.invoked_subcommand is None: # Only run if no subcommand is provided
        main.createFolder_level0()

@app.command()
def create_proxies(
    folder_footage:Annotated[str, typer.Argument(help="Full path to footage folder. (Use '.' for current working directory)")],
    codec:Annotated[str, typer.Option('--codec', '-c', help=f'Supported: {transcode.list_presets()}')]=transcode.detect_defaults('codec'),
    resolution:Annotated[str, typer.Option('--resolution', '-r', help="Ex. '1280x720', '1920x1080', '3840x2160', ...")]=transcode.detect_defaults('resolution')):
    '''Create proxies for footage in the specified footage folder.'''
    transcode.create_proxies(folder_footage, codec, resolution)

@app.command()
def install_ffmpeg():
    '''Install FFmpeg (needed to transcode footage).'''
    ffmpeg_installscript.main()

@app.command()
def version():
    '''Print the current version.'''
    version = initfilm.__version__
    print(version)