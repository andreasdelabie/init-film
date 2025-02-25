import sys, importlib.metadata
import initfilm.main
import initfilm.shortcut
import initfilm.config


def main():
    version = importlib.metadata.version("init-film")


    if len(sys.argv) > 1:
        argument = sys.argv[1]

        if argument == "--help" or argument == "-h":
            print(f'''\
------------------
Init-Film v{version}
By Andreas Delabie
------------------

Usage: init-film [option]
e.g. init-film --set-number-style double

Options:
    --set-number-style <style>      Set number style to default (1. PROJECT FILES) or double (01. PROJECT FILES)
    --set-separator-style <style>   Set separator style to dot (default), underscore, parenthesis or space
    --show-config                   Print current configuration

    --add-shortcut                  Adds the Init-Film shortcut to the Windows context menu (right click menu)
    --remove-shortcut               Removes the Init-Film shortcut to the Windows context menu (right click menu)

    -v --version                    Print current version
    -h --help                       Shows this screen
''')
        
        elif argument == "--set-number-style":
            if len(sys.argv) > 2:
                initfilm.config.setNumberStyle(sys.argv[2])
            else:
                print("Please specify a valid number style like 'default' or 'double'.")
        
        elif argument == "--set-separator-style":
            if len(sys.argv) > 2:
                initfilm.config.setSeparatorStyle(sys.argv[2])
            else:
                print("Please specify a valid separator style like 'dot', 'underscore', 'parenthesis' or 'space'.")
        
        elif argument == "--show-config":
            initfilm.config.show()

        elif argument == "--add-shortcut":
            initfilm.shortcut.add()

        elif argument == "--remove-shortcut":
            initfilm.shortcut.remove()
        
        elif argument == "--version" or argument == "-v":
            print(version)

        else:
            print("Unknown command, use --help or -h for help")


    else:
        initfilm.main.createFolder_level0()