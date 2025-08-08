import ffmpeg, os, pathlib, re
from . import config
from .clearconsole import clearConsole



try:
    default_codec = config.get('proxies', 'default_codec')
    default_resolution = config.get('proxies', 'default_resolution')
except:
    config.set_proxy_codec('h264')
    config.set_proxy_resolution('1280x720')
    default_codec = config.get('proxies', 'default_codec')
    default_resolution = config.get('proxies', 'default_resolution')



def find_folder(folder_footage:str, subfolder:str) -> str:
    """Auto-detect RAW and PROXIES folders in footage folder.
    Args:
        folder_footage (str): Full path to footage folder.
        subfolder (str): Name of the subfolder to find (ex. 'RAW')
    Returns:
        match (str): Matching folder path."""

    matches = []

    for folder in os.listdir(folder_footage):
        if re.match(f'(\d|\d\d)(.\s|\s){subfolder}', folder):
            matches.append(os.path.join(folder_footage, folder))

    if not matches:
        raise FileNotFoundError(f'No folder named "{subfolder}" found in {folder_footage}')

    return matches[0]



def transcode(folder_raw:str, folder_proxies:str, codec:str=default_codec, resolution:str=default_resolution):
    """Main transcode function. Transcodes all files in RAW folder to PROXIES folder.
    Args:
        folder_raw (str): Full path to RAW folder.
        folder_proxies (str): Full path to PROXIES folder.
        codec (str): Codec to use for transcoding (default: 'h264').
        resolution (str): Resolution to use for transcoding (default: '1280x720')."""
    
    for file in os.listdir(folder_raw):
        file_input = os.path.join(folder_raw, file)
        file_output = f'{os.path.join(folder_proxies, pathlib.Path(file).stem)}_proxy_{codec}_{resolution}'

        match codec:
            case 'h264':
                stream = ffmpeg.output(
                    ffmpeg.input(file_input),
                    file_output+'.mp4',
                    **{'c:v':'libx264',
                    'c:a':'copy',
                    'crf':24,
                    'preset':'veryfast'},
                    threads=os.cpu_count(),
                    s=resolution,
                    n=None # Never overwrite files
                )
            case 'dnxhr':
                stream = ffmpeg.output(
                    ffmpeg.input(file_input),
                    file_output+'.mov',
                    **{'c:v':'dnxhd',
                    'c:a':'copy',
                    'profile:v':'dnxhr_lb',
                    'pix_fmt':'yuv422p'},
                    threads=os.cpu_count(),
                    s=resolution,
                    n=None # Never overwrite files
                )
            case 'prores-proxy':
                stream = ffmpeg.output(
                    ffmpeg.input(file_input),
                    file_output+'.mov',
                    **{'c:v':'prores',
                    'c:a':'copy',
                    'profile:v':0},
                    threads=os.cpu_count(),
                    s=resolution,
                    n=None # Never overwrite files
                )
            case 'prores-lt':
                stream = ffmpeg.output(
                    ffmpeg.input(file_input),
                    file_output+'.mov',
                    **{'c:v':'prores',
                    'c:a':'copy',
                    'profile:v':1},
                    threads=os.cpu_count(),
                    s=resolution,
                    n=None # Never overwrite files
                )
                
        ffmpeg.run(stream)



def transcode_footage(folder_footage:str, codec:str=default_codec, resolution:str=default_resolution):
    """Find RAW and PROXIES folders in FOOTAGE folder and transcode files.
    Args:
        folder_footage (str): Full path to footage folder.
        codec (str): Codec to use for transcoding (default: 'h264').
        resolution (str): Resolution to use for transcoding (default: '1280x720')."""

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

            transcode(folder_input, folder_proxies, codec, resolution)
    else:
        transcode(folder_raw, folder_proxies, codec, resolution)