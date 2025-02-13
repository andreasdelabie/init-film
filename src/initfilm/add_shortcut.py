import os, sys, requests


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

        image_data = requests.get("https://github.com/andreasdelabie/init-film/blob/a8777b7cb77b9a099a04a985a70f354024e5317b/logo/Init-Film_Icon.ico").content
        with open(f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\Init-Film_Icon.ico", 'wb') as file:
            file.write(image_data)

        location = winreg.HKEY_CLASSES_ROOT
        shell = winreg.OpenKeyEx(location, r"Directory\\Background\\shell")

        initfilm = winreg.CreateKey(shell, "Init-Film")
        command = winreg.CreateKey(initfilm, "command")

        winreg.SetValueEx(initfilm, "", 0, winreg.REG_SZ, "Start Init-Film Project") # Shortcut name
        winreg.SetValueEx(initfilm, "Icon", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\Init-Film_Icon.ico") # Shortcut icon
        winreg.SetValueEx(command, "", 0, winreg.REG_SZ, f"{user}\AppData\Local\Programs\Python\{python}\Scripts\init-film.exe") # Shortcut executable path
        
        print("Successfully added Init-Film to context menu!")


    except Exception as err:
        print(err, "\nAre you administrator?")