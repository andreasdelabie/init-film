import os, sys


# Get & print python path
pythonVersion = f'{sys.version_info.major}{sys.version_info.minor}'
pythonPath = os.path.expanduser(f'~\\AppData\\Local\\Programs\\Python\\Python{pythonVersion}\\Scripts')
print(f'Python version {pythonVersion} ({pythonPath})')


# Remove script
scriptName = "init-film"
scriptFileName1 = scriptName+"-script.py"
scriptFileName2 = scriptName+".exe"
scriptPath1 = os.path.join(pythonPath, scriptFileName1)
scriptPath2 = os.path.join(pythonPath, scriptFileName2)

if os.path.exists(scriptPath1):
    os.remove(scriptPath1)
    print(f'Uninstalled {scriptName} from {scriptPath1}')
if os.path.exists(scriptPath2):
    os.remove(scriptPath2)
    print(f'Uninstalled {scriptName} from {scriptPath2}')
else:
    print(f'{scriptName} not found in {pythonPath}')