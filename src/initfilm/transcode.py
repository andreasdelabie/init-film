import ffmpeg, os, pathlib



def transcode_folder(folder_input, folder_output, codec, resolution):
    for file in os.listdir(folder_input):
        file_input = os.path.join(folder_input, file)
        file_output = f'{os.path.join(folder_output, pathlib.Path(file).stem)}_proxy_{codec}_{resolution}'
        max_threads = os.cpu_count()

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



transcode_folder('INPUT', 'PROXIES', 'h264', '1280x720')