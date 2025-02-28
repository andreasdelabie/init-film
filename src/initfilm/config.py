import sysconfig, os, json



python_sitepackages = sysconfig.get_path("purelib")

if not os.path.exists(f"{python_sitepackages}/initfilm/config.json"):
    with open(f"{python_sitepackages}/initfilm/config_default.json", "r") as config_default:
        config_default = json.load(config_default)
        with open(f"{python_sitepackages}/initfilm/config.json", "w") as config:
            config.seek(0)
            json.dump(config_default, config, indent=4)
            config.truncate()



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



def setPrefixVisibility(input:str):
    """Set `prefix` `visibility` parameter to input.
    Args:
        input (str): Value to set `visibility` to."""
    
    match input:
        case "visible" | "hidden":
            set("prefix", "visibility", input)
        case _:
            print("Please specify if you want the prefix to be 'visible' or 'hidden'.")



def setNumberStyle(input:str):
    """Set `prefix` `number_style` parameter to input.
    Args:
        input (str): Value to set `number_style` to."""

    match input:
        case "default" | "double":
            set("prefix", "number_style", input)
        case _:
            print("Invalid number style! Valid options are 'default' or 'double'.")



def setSeparatorStyle(input:str):
    """Set `prefix` `separator_style` parameter to input.
    Args:
        input (str): Value to set `separator_style` to."""

    match input:
        case "dot" | "underscore" | "parenthesis" | "space":
            set("prefix", "separator_style", input)
        case _:
            print("Invalid separator style! Valid options are 'dot', 'underscore', 'parenthesis' or 'space'.")