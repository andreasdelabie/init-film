import os, sys


def main():
    osname = os.name
    if osname != 'nt':
        print("This feature currently only works on Windows!")
        exit()
    else:
        import winreg


    try:
        user = os.path.expanduser("~")
        python = f"Python{sys.version_info.major}{sys.version_info.minor}"

        os.remove(f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\Init-Film_Icon.ico")

        location = winreg.HKEY_CLASSES_ROOT
        shell = winreg.OpenKeyEx(location, r"Directory\\Background\\shell")
        initfilm = winreg.CreateKey(shell, "Init-Film")
        command = winreg.CreateKey(initfilm, "command")

        winreg.DeleteValue(command, "")
        winreg.DeleteValue(initfilm, "")
        winreg.DeleteValue(initfilm, "Icon")

        winreg.DeleteKey(command, "")
        winreg.CloseKey(command)
        winreg.DeleteKey(initfilm, "")
        winreg.CloseKey(initfilm)
        
        print("Successfully removed Init-Film from context menu!")


    except Exception as err:
        if str(err).__contains__('WinError 5'):
            print(err, "\n\nAre you administrator?")
        elif str(err).__contains__('WinError 2'):
            print(err, "\n\nThis probably means the shortcut has already been removed, or hasn't been installed correctly...")
        else:
            print(err)