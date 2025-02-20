import os


def main():
    """Removes the Init-Film shortcut to the Windows context menu."""

    
    osname = os.name
    if osname != 'nt':
        print("This feature currently only works on Windows!")
        exit()
    else:
        import winreg


    try:
        location = winreg.HKEY_CLASSES_ROOT
        shell = winreg.OpenKeyEx(location, "Directory\\Background\\shell")
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