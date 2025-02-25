import os, sysconfig, shutil
import initfilm.config



python_sitepackages = sysconfig.get_path("purelib")
template_path = initfilm.config.get("templates", "path")

if template_path == "python":
    template_path = f"{python_sitepackages}/initfilm/templates"
    os.makedirs(template_path, exist_ok=True)
else:
    template_path = template_path
    os.makedirs(template_path, exist_ok=True)



def clearConsole():
    """Clears the console."""

    osname = os.name
    if osname == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For macOS & Linux



def check(relative_source_path:str) -> bool:
    """Checks if source folder contains template files.
    Args:
        relative_source_path (str): Path to template files, relative to `template_path` (ex. "ASSETS/LOGOS")
    Returns:
        result (bool): `True` if folder contains files, `False` if it doesn't."""

    source_path = os.path.join(template_path, relative_source_path)

    try:
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))] # Lists all contents in source_path & only returns files

        if files == []:
            return False
        else:
            return True

    except:
        return False


def copy(relative_source_path:str, destination_path:str, destination_name:str):
    """
    Lists all template files in source folder, let's user select files & copies files to destination.
    Args:
        relative_source_path (str): Path to template files, relative to `template_path` (ex. "ASSETS/LOGOS").
        destination_path (str): Full path to destination folder.
        destination_name (str): Name of the destination folder, used in the selection screen (ex. 1. PROJECT FILES).
    """

    source_path = os.path.join(template_path, relative_source_path)
    files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))] # Lists all contents in source_path & only returns files

    clearConsole()
    print(f'Select needed files for {destination_name}\n')
    for id, template in enumerate(files, start=1):
        print(f'    {id}) {template}')
    print('\nType numbers to select (separate by SPACE)')
    selection = input('$ ').split()

    for id in selection:
        shutil.copy2(f"{source_path}/{files[int(id) - 1]}", destination_path)