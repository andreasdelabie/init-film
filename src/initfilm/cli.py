import sys, importlib.metadata
import initfilm.main
import initfilm.add_shortcut
import initfilm.remove_shortcut
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

Options:
    --set-number-style      Set number style to default (1. PROJECT FILES) or double (01. PROJECT FILES)
    --set-separator-style   Set separator style to dot (default), underscore, parenthesis or space
    --show-config           Print current configuration

    --add-shortcut          Adds the Init-Film shortcut to the Windows context menu (right click menu)
    --remove-shortcut       Removes the Init-Film shortcut to the Windows context menu (right click menu)

    -v --version            Print current version
    -h --help               Shows this screen
''')
        
        elif argument == "--set-number-style":
            initfilm.config.setNumberStyle(sys.argv[2])
        
        elif argument == "--set-separator-style":
            initfilm.config.setSeparatorStyle(sys.argv[2])
        
        elif argument == "--show-config":
            initfilm.config.show()

        elif argument == "--add-shortcut":
            initfilm.add_shortcut.main()

        elif argument == "--remove-shortcut":
            initfilm.remove_shortcut.main()
        
        elif argument == "--version" or argument == "-v":
            print(version)

        else:
            print("Unknown command, use --help or -h for help")


    else:
        initfilm.main.createFolder_level0()