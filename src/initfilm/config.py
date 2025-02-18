import os, sys, json



user = os.path.expanduser("~")
python = f"Python{sys.version_info.major}{sys.version_info.minor}"



def set(name:str, parameter:str, value:str):
    with open(f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\config.json", "r+") as file:
        config = json.load(file)
        config[name][parameter] = value
        file.seek(0)
        json.dump(config, file, indent=4)
        file.truncate()



def get(name:str, parameter:str):
    with open(f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\config.json", "r") as file:
        config = json.load(file)
    return config[name][parameter]



def show():
    with open(f"{user}\AppData\Local\Programs\Python\{python}\Lib\site-packages\initfilm\config.json", "r") as file:
        config = json.dumps(json.load(file), indent=2)
    print(config)



def setNumberStyle(input:str):
    match input:
        case "default" | "double":
            set("prefix", "number_style", input)
        case _:
            print("Invalid number style! Valid options are 'default' or 'double'.")



def setSeparatorStyle(input:str):
    match input:
        case "dot" | "underscore" | "parenthesis" | "space":
            set("prefix", "separator_style", input)
        case _:
            print("Invalid separator style! Valid options are 'dot', 'underscore', 'parenthesis' or 'space'.")