import os, sys


pythonVersion = f'{sys.version_info.major}{sys.version_info.minor}'
pythonPath = os.path.expanduser(f'~\\AppData\\Local\\Programs\\Python\\Python{pythonVersion}\\Scripts')
print(f'Python version {pythonVersion} ({pythonPath})')

scriptName = "init-film-script.py"
scriptPath = os.path.join(pythonPath, scriptName)

if os.path.exists(scriptPath):
    os.remove(scriptPath)
    print(f'Uninstalled {scriptName} from {scriptPath}')
else:
    print(f'{scriptName} not found in {pythonPath}')