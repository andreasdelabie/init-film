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



import os, sysconfig, shutil, yaspin
from . import config
from .clearconsole import clearConsole



python_sitepackages = sysconfig.get_path('purelib')
template_path = config.get('templates', 'path')

if template_path == 'python':
    template_path = f'{python_sitepackages}/initfilm/templates'
    os.makedirs(template_path, exist_ok=True)
else:
    os.makedirs(template_path, exist_ok=True)



def check(relative_source_path:str) -> bool:
    '''Checks if source folder contains template files.
    Args:
        relative_source_path (str): Path to template files, relative to `template_path` (ex. 'ASSETS/LOGOS')
    Returns:
        result (bool): `True` if folder contains files, `False` if it doesn't.'''

    source_path = os.path.join(template_path, relative_source_path)

    try:
        files = [f for f in os.listdir(source_path) if f != '.DS_Store'] # Lists all contents in source_path & excludes .DS_Store files

        if files == []:
            return False
        else:
            return True

    except:
        return False



def copy(relative_source_path:str, destination_path:str, destination_name:str):
    '''Lists all template files in source folder, let's user select files & copies files to destination.
    Args:
        relative_source_path (str): Path to template files, relative to `template_path` (ex. 'ASSETS/LOGOS').
        destination_path (str): Full path to destination folder.
        destination_name (str): Name of the destination folder, used in the selection screen (ex. 1. PROJECT FILES).
    '''

    source_path = os.path.join(template_path, relative_source_path)
    files = [f for f in os.listdir(source_path) if f != '.DS_Store'] # Lists all contents in source_path & excludes .DS_Store files

    clearConsole()
    print(f'Select needed files/folders for {destination_name}\n')
    for id, template in enumerate(files, start=1):
        if os.path.isdir(f'{source_path}/{template}'):
            print(f'    {id}) /{template} (folder)')
            continue
        print(f'    {id}) {template}')
    print('\nType numbers to select (separate by SPACE)')
    selection = input('$ ').split()

    for id in selection:
        template = files[int(id) - 1]

        with yaspin.yaspin(color='yellow', text=f'Copying {template} to {destination_name}...') as spinner:
            if os.path.isdir(f'{source_path}/{template}'):
                # TODO: Respect folder prefixes
                shutil.copytree(f'{source_path}/{template}', f'{destination_path}/{template}', dirs_exist_ok=True)
                continue
            else:
                shutil.copy2(f'{source_path}/{template}', destination_path)
            spinner.text = f'Copying {template} to {destination_name} completed!'
            spinner.ok('✔')