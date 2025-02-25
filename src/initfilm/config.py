import sysconfig, json



python_sitepackages = sysconfig.get_path("purelib")



def set(name:str, parameter:str, value:str):
    """Change values in the config file.
    Args:
        name (str): Name of the config property you want to change. (ex. 'prefix' or 'templates')
        parameter (str): Name of the property parameter you want to change. (ex. 'number_style' or 'path')
        value (str): Value to change the property to. (ex. 'default' or 'dot')"""

    with open(f"{python_sitepackages}/initfilm/config.json", "r+") as file:
        config = json.load(file)
        config[name][parameter] = value
        file.seek(0)
        json.dump(config, file, indent=4)
        file.truncate()



def get(name:str, parameter:str) -> str:
    """Get values from the config file.
    Args:
        name (str): Name of the config property you want to get. (ex. 'prefix' or 'templates')
        parameter (str): Name of the property parameter you want to get. (ex. 'number_style' or 'path')
    Returns:
        value (str): The value of the parameter you defined."""

    with open(f"{python_sitepackages}/initfilm/config.json", "r") as file:
        config = json.load(file)
    return config[name][parameter]



def show():
    """Print current configuration."""

    with open(f"{python_sitepackages}/initfilm/config.json", "r") as file:
        config = json.dumps(json.load(file), indent=2)
    print(f"{python_sitepackages}/initfilm/config.json\n" + config)



def setNumberStyle(input:str):
    """Set `number_style` parameter to input.
    Args:
        input (str): Value to set `number_style` to."""

    match input:
        case "default" | "double":
            set("prefix", "number_style", input)
        case _:
            print("Invalid number style! Valid options are 'default' or 'double'.")



def setSeparatorStyle(input:str):
    """Set `separator_style` parameter to input.
    Args:
        input (str): Value to set `separator_style` to."""

    match input:
        case "dot" | "underscore" | "parenthesis" | "space":
            set("prefix", "separator_style", input)
        case _:
            print("Invalid separator style! Valid options are 'dot', 'underscore', 'parenthesis' or 'space'.")