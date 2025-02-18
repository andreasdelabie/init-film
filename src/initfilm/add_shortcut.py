import os, sys, darkdetect


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
        windows_theme = darkdetect.theme()

        location = winreg.HKEY_CLASSES_ROOT
        shell = winreg.OpenKeyEx(location, r"Directory\\Background\\shell")

        initfilm = winreg.CreateKey(shell, "Init-Film")
        command = winreg.CreateKey(initfilm, "command")

        winreg.SetValueEx(initfilm, "", 0, winreg.REG_SZ, "Start Init-Film Project") # Shortcut name
        winreg.SetValueEx(command, "", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Scripts\init-film.exe") # Shortcut executable path

        if windows_theme == 'Dark':
            winreg.SetValueEx(initfilm, "Icon", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\Init-Film_Icon_White.ico")
        else:
            winreg.SetValueEx(initfilm, "Icon", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\Init-Film_Icon_Black.ico")
        
        print("Successfully added Init-Film to context menu!")


    except Exception as err:
        if str(err).__contains__('WinError 5'):
            print(err, "\n\nAre you administrator?")
        else:
            print(err)