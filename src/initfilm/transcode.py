import ffmpeg, os, pathlib, re
from .clearconsole import clearConsole



def find_folder(folder_footage, subfolder):
    folders = []

    for folder in os.listdir(folder_footage):
        if re.match(f'(\d|\d\d)(.\s|\s){subfolder}', folder):
            folders.append(os.path.join(folder_footage, folder))

    return folders[0]



def transcode_folder(folder_footage, codec='h264', resolution='1280x720'):
    folder_raw = find_folder(folder_footage, 'RAW')
    folder_proxies = find_folder(folder_footage, 'PROXIES')
    max_threads = os.cpu_count()

    clearConsole()
    print(f'Select folders to transcode:\n(You can always do this later! See --help)\n')
    for id, folder in enumerate(os.listdir(folder_raw), start=1):
        print(f'    {id}) {folder}')
    print('\nType numbers to select (separate by SPACE)')
    folder_selection = input('$ ').split()

    clearConsole()
    print(f'Select codec (supported: h264, dnxhr, prores-proxy, prores-lt):')
    codec = input('$ ')
    if not codec: codec = 'h264'

    clearConsole()
    print(f'Select resolution (ex. 1280x720):')
    resolution = input('$ ')
    if not resolution: resolution = '1280x720'

    for id in folder_selection:
        folder = folder_selection[int(id) - 1]
        print(f'Transcoding {folder} to {codec} {resolution}...')

        for file in os.listdir(folder):
            file_input = os.path.join(folder, file)
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
                        threads=max_threads,
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
                        threads=max_threads,
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
                        threads=max_threads,
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
                        threads=max_threads,
                        s=resolution,
                        n=None # Never overwrite files
                    )
                    
            ffmpeg.run(stream)