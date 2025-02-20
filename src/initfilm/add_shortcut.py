import os, sysconfig, darkdetect


def main():
    """Adds the Init-Film shortcut to the Windows context menu."""
    

    osname = os.name
    if osname != 'nt':
        print("This feature currently only works on Windows!")
        exit()
    else:
        import winreg


    try:
        python_scripts = sysconfig.get_path("scripts")
        python_sitepackages = sysconfig.get_path("purelib")
        windows_theme = darkdetect.theme()

        location = winreg.HKEY_CLASSES_ROOT
        shell = winreg.OpenKeyEx(location, "Directory\\Background\\shell")

        initfilm = winreg.CreateKey(shell, "Init-Film")
        command = winreg.CreateKey(initfilm, "command")

        winreg.SetValueEx(initfilm, "", 0, winreg.REG_SZ, "Start Init-Film Project") # Shortcut name
        winreg.SetValueEx(command, "", 0, winreg.REG_SZ, f"{python_scripts}/init-film.exe") # Shortcut executable path

        if windows_theme == 'Dark':
            winreg.SetValueEx(initfilm, "Icon", 0, winreg.REG_SZ, f"{python_sitepackages}/initfilm/Init-Film_Icon_White.ico")
        else:
            winreg.SetValueEx(initfilm, "Icon", 0, winreg.REG_SZ, f"{python_sitepackages}/initfilm/Init-Film_Icon_Black.ico")
        
        print("Successfully added Init-Film to context menu!")


    except Exception as err:
        if str(err).__contains__('WinError 5'):
            print(err, "\n\nAre you administrator?")
        else:
            print(err)