import os


def main():
    osname = os.name
    if osname != 'nt':
        print("This feature currently only works on Windows!")
        exit()
    else:
        import winreg


    try:
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
        print(err, "\nAre you administrator?")