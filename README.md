# Init-Film  
![image](https://github.com/user-attachments/assets/9d9dd462-6b83-4ac7-a3d9-4efb88e4fb72)  
Tired of manually creating folder structures for your film/video projects?  
Want a folder structure that dynamically changes based on the needs for your project?  
Then Init-Film was made for you!  
By filmmakers, for filmmakers ;)  


### Key features:  
- ♥️ Supports Windows, Linux, and macOS
- ✅ Dynamically create folder structures by selecting options from a list  
- 🖋️ Use custom folder names  
- [📝](https://github.com/andreasdelabie/init-film/?tab=readme-ov-file#templates) Import file templates & project assets to reuse across multiple projects  
- [✨](https://github.com/andreasdelabie/init-film/?tab=readme-ov-file#configuration) Customize the prefix style to your preference!
- [📋](https://github.com/andreasdelabie/init-film/?tab=readme-ov-file#copy-project-title-to-clipboard) Auto copies the project title to your clipboard
- [🖱️](https://github.com/andreasdelabie/init-film/?tab=readme-ov-file#add-shortcut-to-windows-context-menu-right-click-menu) Start a new project by right-clicking in a folder and selecting "Start Init-Film Project" *(Windows only)*  
### ->>[Watch showcase](https://www.youtube.com/watch?v=QheWe-1PqUM)<<-  


## Before installing:  
Make sure you have any of the following [Python](https://www.python.org/) versions installed (tested with tox):  
| Version                                                             | Comments               |
| ------------------------------------------------------------------- | ---------------------- |
| [3.14](https://www.python.org/downloads/release/python-3140rc2/)    | testing                |
| **[3.13](https://www.python.org/downloads/release/python-3137/)**   | recommended            |
| [3.12](https://www.python.org/downloads/release/python-31210/)      |                        |
| [3.11](https://www.python.org/downloads/release/python-3119/)       |                        |
| [3.10](https://www.python.org/downloads/release/python-31011/)      |                        |
| [3.9](https://www.python.org/downloads/release/python-3913/)        | dropping support soon! |


## Installation:  
### Method 1 (from PyPi):  
[Watch YouTube tutorial](https://www.youtube.com/watch?v=Z5_rhFlNFM8)  
Use `pip install init-film` to install the latest version of init-film.  

### Method 2 (from source):  
[Watch YouTube tutorial](https://www.youtube.com/watch?v=oiKy_RU5WHE)  
1. Download the repo by using `git clone https://github.com/andreasdelabie/init-film` or download the zip folder from the [releases](https://github.com/andreasdelabie/init-film/releases).  
2. Navigate to the folder by using `cd [path to folder]` or using a file explorer.  
3. Use `pip install .` to install the script.  

### Error: externally-managed-environment
![image](https://github.com/user-attachments/assets/71cae57b-8baf-4a1f-b0ac-3bbf978bff38)  
Check out the documentation for [externally managed environments](https://github.com/andreasdelabie/init-film/blob/main/README-ExternallyManagedEnvironments.md).  


## Usage:  
[Watch showcase](https://www.youtube.com/watch?v=QheWe-1PqUM)  

### Basic usage:  
Use the CLI command `init-film` in any folder to start a new film/video project.  

### Custom folder names:  
Folder names can't contain spaces (with the exception of the project name). Instead use a `-` or `_`.  

### Configuration:  
- Use `init-film --set-prefix <option>` to set the prefix to `visible` (default) or `hidden`.
- Use `init-film --set-number-style <style>` to set the number style to `default` (1. PROJECT FILES) or `double` (01. PROJECT FILES).  
- Use `init-film --set-separator-style <style>` to set the separator style to `dot` (default), `underscore`, `parenthesis`, or `space`.  
- Use `init-film --set-templates-path` to set the template path to `python` (`.../site-packages/initfilm/templates`) or a custom path (ex. `C:/Users/Spielberg/Videos/templates`). Make sure to <ins>ALWAYS USE FORWARD SLASHES</ins>!  
- Use `init-film --show-config` to print the current configuration and the path to the `config.json` file.  

### Templates:  
Put your template files in the relative template folders (use `init-film --show-templates-path` to show the location).  
Init-Film will automatically detect them and let you select them when creating a new project.  
#### Example:  
If I use the following folder structure:  
```
1. PROJECT FILES
  1. PREMIERE PRO
  2. AFTER EFFECTS
2. ASSETS
  1. LOGOS
  2. GRAPHICS
3. FOOTAGE
4. AUDIO
  1. SFX
  2. MUSIC
5. EXPORT
6. CUSTOM-FOLDER
```
I put the template files in the templates folder like this:  
```
PROJECT FILES
  PREMIERE PRO
    YouTube_Video_Preset.prproj
  AFTER EFFECTS
    Animation_Preset.aep
ASSETS
  LOGOS
    Logo1.png
    Logo2.jpg
  GRAPHICS
    Explosion.mov
    Title.ai
AUDIO
  SFX
    Explosion.wav
    Whoosh.mp3
  MUSIC
    Theme_Song.wav
    Outro_Song.wav
CUSTOM-FOLDER
  Custom_Folder_Template_File.docx
```

### Copy project title to clipboard:
After you have entered the project title, it will automatically get copied to your clipboard.  
On Linux, you may have to install a clipboard manager like [xclip](https://github.com/astrand/xclip).  
- Debian/Ubuntu based systems: `sudo apt install xclip`  
- Arch/Manjaro based systems: `sudo pacman -S xclip`  
- Fedora based systems: `sudo dnf install xclip`  

### Add shortcut to Windows context menu (right click menu):  
- Use `init-film --add-shortcut` to add Init-Film to your Windows context menu.  
- Use `init-film --remove-shortcut` to remove it.  


### Help:  
Use `init-film --help` or `init-film -h` to show the help screen.  


## Updating:  
Use `pip install --upgrade init-film` to update to the latest version of init-film.  


## Uninstalling:  
Use `pip uninstall init-film` to fully uninstall init-film from your system.  


## Support:  
[!["Buy Me A Coffee"](https://buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://buymeacoffee.com/andreasdelabie)
