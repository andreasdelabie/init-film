import os, sysconfig, darkdetect



def add():
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

        location = winreg.HKEY_CURRENT_USER
        shell = winreg.CreateKey(location, "Software\\Classes\\Directory\\Background\\shell")
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



def remove():
    """Removes the Init-Film shortcut to the Windows context menu."""

    
    osname = os.name
    if osname != 'nt':
        print("This feature currently only works on Windows!")
        exit()
    else:
        import winreg


    try:
        location = winreg.HKEY_CURRENT_USER
        shell = winreg.CreateKey(location, "Software\\Classes\\Directory\\Background\\shell")
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