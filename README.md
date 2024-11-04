# Init-Film  
![image](https://github.com/user-attachments/assets/9d9dd462-6b83-4ac7-a3d9-4efb88e4fb72)  
Tired of manually creating folder structures for your film/video projects?  
Want a folder structure that dynamically changes based on the needs for your project?  
Then Init-Film was made for you!  
By filmmakers, for filmmakers ;)  

## Before installing:  
Make sure you have any of the following [Python](https://www.python.org/) versions installed (tested with tox):  
  - [3.13](https://www.python.org/downloads/release/python-3130/) (recommended)  
  - [3.12](https://www.python.org/downloads/release/python-3127/)  
  - [3.11](https://www.python.org/downloads/release/python-3119/)  
  - [3.10](https://www.python.org/downloads/release/python-31011/)  
  - [3.9](https://www.python.org/downloads/release/python-3913/)  
  - [3.8](https://www.python.org/downloads/release/python-3810/)  

## Installation:  
[Watch YouTube tutorial](https://www.youtube.com/watch?v=NGrjQcJ-8Xs)  
1. Download the repo by typing `git clone https://github.com/andreasdelabie/init-film` in a terminal or download the zip folder directly from the GitHub page.  
2. Navigate to the folder by using `cd (path to repo)` or using a file explorer.  
3. Install all the Python requirements by using `pip install -r requirements.txt`.  
4. Run the setup script by using `python setup.py install` (or `python setup.py develop` if you encounter errors).  
5. **Don't remove the installation folder, as it contains the source code for the CLI script.**  
Deleting this folder will break the thing and makes uninstalling a pain :(  

## Usage:  
Use the CLI command `init-film` in any folder to start a new film/video project.  
### Custom folder names:  
Folder names can't contain spaces. Instead use a `-` or `_`.  

## Uninstalling:  
1. Navigate to the installation folder by using `cd (path to repo)` or using a file explorer.  
2. Remove all the script files by using `python uninstall.py`.  
3. Check that there is no file named `init_film-(version).egg` in `user\appdata\local\programs\python\python(version)\lib\site-packages\`  
4. You can now safely delete the installation folder.  

## Support:  
<a href="https://www.buymeacoffee.com/andreasdelabie"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=andreasdelabie&button_colour=FFDD00&font_colour=000000&font_family=Comic&outline_colour=000000&coffee_colour=ffffff"/></a>  
