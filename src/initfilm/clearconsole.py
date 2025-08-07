import os



def clearConsole():
    """Clears the console."""

    osname = os.name
    if osname == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For macOS & Linux