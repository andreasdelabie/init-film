import os, sys, shutil
version = '1.1.0'


def showTitle():
    print('---------------------\nINIT-FILM UNINSTALLER\n---------------------')


def getPythonPath():
    global pythonVersion, pythonPath
    pythonVersion = f'{sys.version_info.major}{sys.version_info.minor}'
    pythonPath = os.path.expanduser(f'~\\AppData\\Local\\Programs\\Python\\Python{pythonVersion}')

    print(f'Python version: {pythonVersion}\nPath: {pythonPath}\n---------------------')


def removeFiles():
    files = [
        os.path.join(pythonPath, 'Scripts\init-film.exe'),
        os.path.join(pythonPath, f'Lib\\site-packages\\init_film-{version}.dist-info'),
        os.path.join(pythonPath, f'Lib\\site-packages\\initfilm')
    ]

    for file in files:
        if os.path.exists(file):
            if os.path.isfile(file):
                os.remove(file)
            elif os.path.isdir(file):
                shutil.rmtree(file)
            print(f'[REMOVED] {file}')
        else:
            print(f'[SKIPPED] {file} (not found or already removed)')


def main():
    showTitle()
    getPythonPath()
    removeFiles()


main()