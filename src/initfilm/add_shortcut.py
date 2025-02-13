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

        location = winreg.HKEY_CLASSES_ROOT
        shell = winreg.OpenKeyEx(location, r"Directory\\Background\\shell")

        initfilm = winreg.CreateKey(shell, "Init-Film")
        command = winreg.CreateKey(initfilm, "command")

        winreg.SetValueEx(initfilm, "", 0, winreg.REG_SZ, "Start Init-Film Project") # Shortcut name
        winreg.SetValueEx(initfilm, "Icon", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Scripts\init-film.exe") # Shortcut icon
        winreg.SetValueEx(command, "", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Scripts\init-film.exe") # Shortcut executable path
        
        print("Successfully added Init-Film to context menu!")


    except Exception as err:
        print(err, "\nAre you administrator?")