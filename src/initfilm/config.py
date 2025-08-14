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



import sysconfig, os, json, typer



python_sitepackages = sysconfig.get_path('purelib')
app = typer.Typer(add_completion=False)

if not os.path.exists(f'{python_sitepackages}/initfilm/config.json'):
    with open(f'{python_sitepackages}/initfilm/config_default.json', 'r') as config_default:
        config_default = json.load(config_default)
        with open(f'{python_sitepackages}/initfilm/config.json', 'w') as config:
            config.seek(0)
            json.dump(config_default, config, indent=4)
            config.truncate()



def set(name:str, parameter:str, value:str):
    '''Change values in the config file.
    Args:
        name (str): Name of the config property you want to change. (ex. 'prefix' or 'templates')
        parameter (str): Name of the property parameter you want to change. (ex. 'number_style' or 'path')
        value (str): Value to change the property to. (ex. 'default' or 'dot')'''

    with open(f'{python_sitepackages}/initfilm/config.json', 'r+') as file:
        config = json.load(file)
        if name not in config:
            config[name] = {}  # Create section if missing
        config[name][parameter] = value
        file.seek(0)
        json.dump(config, file, indent=4)
        file.truncate()



def get(name:str, parameter:str) -> str:
    '''Get values from the config file.
    Args:
        name (str): Name of the config property you want to get. (ex. 'prefix' or 'templates')
        parameter (str): Name of the property parameter you want to get. (ex. 'number_style' or 'path')
    Returns:
        value (str): The value of the parameter you defined.'''

    with open(f'{python_sitepackages}/initfilm/config.json', 'r') as file:
        config = json.load(file)
    return config[name][parameter]     



@app.command()
def set_prefix_visibility(visibility:str):
    '''Set prefix visibility to 'visible' or 'hidden'.'''
    match input:
        case 'visible' | 'hidden':
            set('prefix', 'visibility', visibility)
        case _:
            print("Please specify if you want the prefix to be 'visible' or 'hidden'.")

@app.command()
def set_number_style(style:str):
    '''Set number style to 'default' or 'double'.'''
    match style:
        case 'default' | 'double':
            set('prefix', 'number_style', style)
        case _:
            print("Invalid number style! Valid options are 'default' or 'double'.")

@app.command()
def set_separator_style(style:str):
    '''Set separator style to 'dot', 'underscore', 'parenthesis' or 'space'.'''
    match style:
        case 'dot' | 'underscore' | 'parenthesis' | 'space':
            set('prefix', 'separator_style', style)
        case _:
            print("Invalid separator style! Valid options are 'dot', 'underscore', 'parenthesis' or 'space'.")

@app.command()
def set_templates_path(path:str):
    '''Set templates path (source path) to 'python' or custom path. ALWAYS USE FORWARD SLASHES!'''
    set('templates', 'path', path)

@app.command()
def set_proxy_codec(codec:str):
    '''Set default proxy codec to 'h264', 'h264-nvidia', 'h264-amd', 'h264-intel', 'dnxhr', 'prores-proxy' or 'prores-lt'.'''
    match codec:
        case 'h264' | 'h264-nvidia' | 'h264-amd' | 'h264-intel' | 'dnxhr' | 'prores-proxy' | 'prores-lt':
            set('proxies', 'default_codec', codec)
        case _:
            print("Invalid codec! Valid options are 'h264', 'h264-nvidia', 'h264-amd', 'h264-intel', 'dnxhr', 'prores-proxy' or 'prores-lt'.")

@app.command()
def set_proxy_resolution(resolution:str):
    '''Set default proxy resolution. (ex. '1280x720', '1920x1080', '3840x2160', ...).'''
    set('proxies', 'default_resolution', resolution)

@app.command()
def show():
    '''Print the current configuration.'''
    with open(f'{python_sitepackages}/initfilm/config.json', 'r') as file:
        config = json.dumps(json.load(file), indent=2)
    print(f'{python_sitepackages}/initfilm/config.json\n' + config)

@app.command()
def add_shortcut():
    '''Adds the Init-Film shortcut to the Windows context menu (right click menu).'''
    from . import shortcut
    shortcut.add()

@app.command()
def remove_shortcut():
    '''Removes the Init-Film shortcut from the Windows context menu (right click menu).'''
    from . import shortcut
    shortcut.remove()