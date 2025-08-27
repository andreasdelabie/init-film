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



import os, pathlib, re, platform, subprocess, sysconfig, json
from . import config
from .clearconsole import clearConsole



PLATFORM = platform.system().lower()
python_sitepackages = sysconfig.get_path('purelib')



def find_folder(folder_footage:str, subfolder:str) -> str:
    '''Auto-detect RAW and PROXIES folders in footage folder.
    Args:
        folder_footage (str): Full path to footage folder.
        subfolder (str): Name of the subfolder to find (ex. 'RAW')
    Returns:
        match (str): Matching folder path.'''

    matches = []

    for folder in os.listdir(folder_footage):
        if re.match(f'(\d|\d\d)(.\s|\s){subfolder}', folder): # Match folder names like '01 RAW', '2. PROXIES', etc.
            matches.append(os.path.join(folder_footage, folder))

    if not matches:
        raise FileNotFoundError(f"No folder named '{subfolder}' found in {folder_footage}")

    return matches[0]



def list_presets() -> str:
    '''List all available FFmpeg codec presets.'''

    with open(f'{python_sitepackages}/initfilm/ffmpeg_presets.json', 'r') as file:
        presets = json.load(file)
        presets_list = list(presets.keys())

    return str(presets_list)[1:-1] # Remove brackets from list string



def detect_defaults(returns:str) -> str:
    '''Detect default settings for transcoding. Set defaults if not already set.
    Args:
        returns (str): The setting to return (ex. 'codec', 'resolution').
    Returns:
        value (str): The value of the requested setting.'''

    global default_codec, default_resolution

    try:
        default_codec = config.get('proxies', 'default_codec')
        default_resolution = config.get('proxies', 'default_resolution')
    except:
        config.set_proxy_codec('h264')
        config.set_proxy_resolution('1280x720')
        default_codec = config.get('proxies', 'default_codec')
        default_resolution = config.get('proxies', 'default_resolution')

    match returns:
        case 'codec':
            return default_codec
        case 'resolution':
            return default_resolution
        


def get_preset(codec:str) -> str:
    '''Get the FFmpeg preset for the given codec and platform.
    Args:
        codec (str): The codec to get the preset for.
    Returns:
        preset (str): The FFmpeg preset for the given codec and platform. **Needs to be formatted!**  
        ex: `get_preset('h264').format(file_input=os.path.join(folder_raw,file))`'''

    with open(f'{python_sitepackages}/initfilm/ffmpeg_presets.json', 'r') as file:
        presets = json.load(file)

    try:
        return presets[codec][PLATFORM]
    except KeyError:
        try:
            return presets[codec]['generic']
        except KeyError:
            raise NotImplementedError (f"Codec '{codec}' is not supported on your platform ({PLATFORM})")



def transcode(folder_raw:str, folder_proxies:str, codec:str=detect_defaults('codec'), resolution:str=detect_defaults('resolution'), filename:str=config.get('proxies', 'filename')):
    '''Transcode all video files in RAW folder to PROXIES folder.
    Args:
        folder_raw (str): Full path to RAW folder.
        folder_proxies (str): Full path to PROXIES folder.
        codec (str): Codec to use for transcoding.
        resolution (str): Resolution to use for transcoding.
        filename (str): Filename format.'''
    
    for file in os.listdir(folder_raw):
        if not file.lower().endswith(('.mp4', '.mov', '.avi', '.mts', '.mxf', '.mkv', '.wmv', '.flv')): # Only process video files
            continue

        preset = get_preset(codec).format(
            file_input = os.path.join(folder_raw, file),
            file_output = f'{os.path.join(folder_proxies, pathlib.Path(file).stem)}_Proxy' if filename == 'simple' else f'{os.path.join(folder_proxies, pathlib.Path(file).stem)}_proxy_{codec}_{resolution}',
            resolution=resolution,
            w = resolution.split('x')[0],
            h = resolution.split('x')[1],
            threads=os.cpu_count()
        )

        print(f'Transcoding {file} to {codec} {resolution}...')
        subprocess.run(preset, shell=True, check=True)



def create_proxies(folder_footage:str, codec:str=detect_defaults('codec'), resolution:str=detect_defaults('resolution'), filename:str=config.get('proxies', 'filename')):
    '''Find RAW and PROXIES folders in FOOTAGE folder and create proxies.
    Args:
        folder_footage (str): Full path to footage folder. (Use '.' for current working directory)
        codec (str): Codec to use for transcoding.
        resolution (str): Resolution to use for transcoding.
        filename (str): Filename format.'''

    if folder_footage == '.':
        folder_footage = os.getcwd()
    folder_raw = find_folder(folder_footage, 'RAW')
    subfolders_raw = sorted([f for f in os.listdir(folder_raw) if os.path.isdir(os.path.join(folder_raw, f))])
    folder_proxies = find_folder(folder_footage, 'PROXIES')

    if subfolders_raw:
        clearConsole()
        print(f'Select folders to transcode:\n')
        for id, folder in enumerate(subfolders_raw, start=1):
            print(f'    {id}) {folder}')
        print('\nType numbers to select (separate by SPACE)')
        folder_selection = input('$ ').split()

        for id in folder_selection:
            folder_input = subfolders_raw[int(id) - 1]
            folder_input = os.path.join(folder_raw, folder_input)

            transcode(folder_input, folder_proxies, codec, resolution, filename)
    else:
        transcode(folder_raw, folder_proxies, codec, resolution, filename)
