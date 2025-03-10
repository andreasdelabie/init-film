import os, pyperclip
import initfilm.config
import initfilm.templates



def clearConsole():
    """Clears the console."""

    osname = os.name
    if osname == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For macOS & Linux



def prefix(number_input:int) -> str:
    """Returns a styled prefix based on the values in the config file.
    Args:
        number_input (int): The prefix number.
    Returns:
        prefix (str): Styled prefix with a number and separator."""

    try:
        visible = initfilm.config.get("prefix", "visibility")
    except:
        initfilm.config.setPrefixVisibility("visible")
        visible = initfilm.config.get("prefix", "visibility")
    number_style = initfilm.config.get("prefix", "number_style")
    separator_style = initfilm.config.get("prefix", "separator_style")

    if number_style == "double":
        number_output = f"{number_input:02d}"
    else:
        number_output = number_input
    
    if separator_style == "underscore":
        separator = "_"
    elif separator_style == "parenthesis":
        separator = ") "
    elif separator_style == "space":
        separator = " "
    else:
        separator = ". "
    
    if visible == "hidden":
        return ""
    else:
        return f"{number_output}{separator}"



def createFolder_level0():
    global projectDirectory, workingTitle

    clearConsole()
    print('Enter project name:')

    workingTitle = input('$ ')
    pyperclip.copy(workingTitle)
    currentDirectory = os.getcwd()
    projectDirectory = os.path.join(currentDirectory, workingTitle)

    os.mkdir(projectDirectory)
    if initfilm.templates.check("") == True:
        initfilm.templates.copy("", projectDirectory, workingTitle)

    createFolder_level1_project()



def createFolder_level1(number:int, name:str):
    global level1_folder_name
    level1_folder_name = f'{prefix(number)}{name}'
    level1_folder_directory = os.path.join(projectDirectory, level1_folder_name)

    os.mkdir(level1_folder_directory)
    if initfilm.templates.check(name) == True:
        initfilm.templates.copy(name, level1_folder_directory, level1_folder_name)



def createFolder_level1_project():
    clearConsole()
    print(f'''Select needed level 1 folders for {workingTitle}

    1) PROJECT FILES
    2) ASSETS
    3) FOOTAGE
    4) AUDIO
    5) EXPORT
    6) DOCUMENTS
    7) MARKETING

Type numbers to select or type custom folder names (separate by SPACE)''')

    level1_project_selection = input('$ ').split()
    global level1_project_folderNumber
    level1_project_folderNumber = 1

    for string in level1_project_selection:
        if string == '1':
            createFolder_level1(level1_project_folderNumber, 'PROJECT FILES')
            createFolder_level2_projectFiles()
        elif string == '2':
            createFolder_level1(level1_project_folderNumber, 'ASSETS')
            createFolder_level2_assets()
        elif string == '3':
            createFolder_level1(level1_project_folderNumber, 'FOOTAGE')
            createFolder_level2_footage()
        elif string == '4':
            createFolder_level1(level1_project_folderNumber, 'AUDIO')
            createFolder_level2_audio()
        elif string == '5':
            createFolder_level1(level1_project_folderNumber, 'EXPORT')
            createFolder_level2_export()
        elif string == '6':
            createFolder_level1(level1_project_folderNumber, 'DOCUMENTS')
            createFolder_level2_documents()
        elif string == '7':
            createFolder_level1(level1_project_folderNumber, 'MARKETING')
            createFolder_level2_marketing()
        else:
            createFolder_level1(level1_project_folderNumber, string.upper())
            createFolder_level2_custom(f'{prefix(level1_project_folderNumber)}{string.upper()}', string.upper())
        level1_project_folderNumber = level1_project_folderNumber + 1



def createFolder_level2(parent:str, number:int, name:str, relative_template_path:str):
    global level2_folder_name
    level2_folder_name = f'{prefix(number)}{name}'
    level2_folder_directory = os.path.join(projectDirectory, parent, level2_folder_name)

    os.mkdir(level2_folder_directory)
    if initfilm.templates.check(relative_template_path) == True:
        initfilm.templates.copy(relative_template_path, level2_folder_directory, level2_folder_name)



def createFolder_level2_projectFiles():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}:

    EDITING:
        1) PREMIERE PRO
        2) DAVINCI RESOLVE
        3) MEDIA COMPOSER
        4) FINAL CUT PRO
        5) SONY VEGAS
        6) HITFILM EXPRESS

    GRAPHICS/VFX:
        7) AFTER EFFECTS
        8) PHOTOSHOP
        9) ILLUSTRATOR
        10) BLENDER
        11) CINEMA 4D
        12) MAYA
        13) NUKE
        14) HOUDINI
        15) ZBRUSH
        16) AFFINITY DESIGNER

    AUDIO/MUSIC:
        17) PRO TOOLS
        18) ABLETON
        19) CUBASE
        20) REAPER
        21) IZOTOPE RX
        22) AUDITION
        23) AUDACITY
        24) LOGIC PRO
        25) FL STUDIO

Type numbers to select or type custom folder names (separate by SPACE)''')

    level2_projectFiles_selection = input('$ ').split()
    level2_projectFiles_folderNumber = 1

    for string in level2_projectFiles_selection:
        if string == '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'PREMIERE PRO', "PROJECT FILES/PREMIERE PRO")
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'DAVINCI RESOLVE', "PROJECT FILES/DAVINCI RESOLVE")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'MEDIA COMPOSER', "PROJECT FILES/MEDIA COMPOSER")
        elif string == '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'FINAL CUT PRO', "PROJECT FILES/FINAL CUT PRO")
        elif string == '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'SONY VEGAS', "PROJECT FILES/SONY VEGAS")
        elif string == '6': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'HITFILM EXPRESS', "PROJECT FILES/HITFILM EXPRESS")
        elif string == '7': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AFTER EFFECT', "PROJECT FILES/AFTER EFFECTS")
        elif string == '8': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'PHOTOSHOP', "PROJECT FILES/PHOTOSHOP")
        elif string == '9': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'ILLUSTRATOR', "PROJECT FILES/ILLUSTRATOR")
        elif string == '10': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'BLENDER', "PROJECT FILES/BLENDER")
        elif string == '11': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'CINEMA 4D', "PROJECT FILES/CINEMA 4D")
        elif string == '12': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'MAYA', "PROJECT FILES/MAYA")
        elif string == '13': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'NUKE', "PROJECT FILES/NUKE")
        elif string == '14': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'HOUDINI', "PROJECT FILES/HOUDINI")
        elif string == '15': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'ZBRUSH', "PROJECT FILES/ZBRUSH")
        elif string == '16': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AFFINITY DESIGNER', "PROJECT FILES/AFFINITY DESIGNER")
        elif string == '17': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'PRO TOOLS', "PROJECT FILES/PRO TOOLS")
        elif string == '18': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'ABLETON', "PROJECT FILES/ABLETON")
        elif string == '19': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'CUBASE', "PROJECT FILES/CUBASE")
        elif string == '20': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'REAPER', "PROJECT FILES/REAPER")
        elif string == '21': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'IZOTOPE RX', "PROJECT FILES/IZOTOPE RX")
        elif string == '22': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AUDITION', "PROJECT FILES/AUDITION")
        elif string == '23': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AUDACITY', "PROJECT FILES/AUDACITY")
        elif string == '24': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'LOGIC PRO', "PROJECT FILES/LOGIC PRO")
        elif string == '25': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'FL STUDIO', "PROJECT FILES/FL STUDIO")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, string.upper(), f"PROJECT FILES/{string.upper()}")
        level2_projectFiles_folderNumber = level2_projectFiles_folderNumber + 1



def createFolder_level2_assets():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}

    1. LOGOS
    2. GRAPHICS
    3. FONTS
    4. OVERLAYS
    5. REFERENCE

Type custom folder names (separate by SPACE)''')

    level2_assets_selection = input('$ ').split()
    level2_assets_folderNumber = 1

    for string in level2_assets_selection:
        if string == '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'LOGOS', "ASSETS/LOGOS")
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'GRAPHICS', "ASSETS/GRAPHICS")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'FONTS', "ASSETS/FONTS")
        elif string == '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'OVERLAYS', "ASSETS/OVERLAYS")
        elif string == '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'REFERENCE', "ASSETS/REFERENCE")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, string.upper(), f"ASSETS/{string.upper()}")
        level2_assets_folderNumber = level2_assets_folderNumber + 1



def createFolder_level2_footage():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}
    
    1) RAW
    2) PROXIES
    3) STOCK
    4) VFX
    5) GRADED
          
Type numbers to select or type custom folder names (separate by SPACE)''')

    level2_footage_selection = input('$ ').split()
    global level2_footage_folderNumber
    level2_footage_folderNumber = 1

    for string in level2_footage_selection:
        if string == '1':
            createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'RAW', "FOOTAGE/RAW")
            createFolder_level3_raw()
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'PROXIES', "FOOTAGE/PROXIES")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'STOCK', "FOOTAGE/STOCK")
        elif string == '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'VFX', "FOOTAGE/VFX")
        elif string == '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'GRADED', "FOOTAGE/GRADED")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, string.upper(), f"FOOTAGE/{string.upper()}")
        level2_footage_folderNumber = level2_footage_folderNumber + 1



def createFolder_level2_audio():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}

    1) PFX
    2) SFX
    3) FOLEY
    4) AMBIANCE
    5) MUSIC
    6) SOUNDTRACK
    7) VOICEOVER
    8) ADR

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_audio_selection = input('$ ').split()
    level2_audio_folderNumber = 1

    for string in level2_audio_selection:
        if string == '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'PFX', "AUDIO/PFX")
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'SFX', "AUDIO/SFX")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'FOLEY', "AUDIO/FOLEY")
        elif string == '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'AMBIANCE', "AUDIO/AMBIANCE")
        elif string == '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'MUSIC', "AUDIO/MUSIC")
        elif string == '6': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'SOUNDTRACK', "AUDIO/SOUNDTRACK")
        elif string == '7': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'VOICEOVER', "AUDIO/VOICEOVER")
        elif string == '8': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'ADR', "AUDIO/ADR")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_selection, string.upper(), f"AUDIO/{string.upper()}")
        level2_audio_folderNumber = level2_audio_folderNumber + 1



def createFolder_level2_export():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}

    1) PREVIEWS
    2) MASTER
    3) DELIVERABLES

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_export_selection = input('$ ').split()
    level2_export_folderNumber = 1

    for string in level2_export_selection:
        if string == '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, 'PREVIEWS', "EXPORT/PREVIEWS")
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, 'MASTER', "EXPORT/MASTER")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, 'DELIVERABLES', "EXPORT/DELIVERABLES")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, string.upper(), f"EXPORT/{string.upper()}")
        level2_export_folderNumber = level2_export_folderNumber + 1



def createFolder_level2_documents():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}
    
    1) NOTES
    2) MOODBOARD
    3) STORYBOARD
    4) SCRIPT
    5) PITCH
    6) LEGAL
    7) FINANCIAL

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_documents_selection = input('$ ').split()
    level2_documents_folderNumber = 1

    for string in level2_documents_selection:
        if string == '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'NOTES', "DOCUMENTS/NOTES")
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'MOODBOARD', "DOCUMENTS/MOODBOARD")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'STORYBOARD', "DOCUMENTS/STORYBOARD")
        elif string == '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'SCRIPT', "DOCUMENTS/SCRIPT")
        elif string == '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'PITCH', "DOCUMENTS/PITCH")
        elif string == '6': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'LEGAL', "DOCUMENTS/LEGAL")
        elif string == '7': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'FINANCIAL', "DOCUMENTS/FINANCIAL")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, string.upper(), f"DOCUMENTS/{string.upper()}")
        level2_documents_folderNumber = level2_documents_folderNumber + 1



def createFolder_level2_marketing():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_folder_name}
    
    1) POSTERS
    2) SOCIAL MEDIA
    3) TRAILERS
    
Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_marketing_selection = input('$ ').split()
    level2_marketing_folderNumber = 1

    for string in level2_marketing_selection:
        if string == '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, 'POSTERS', "MARKETING/POSTERS")
        elif string == '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, 'SOCIAL MEDIA', "MARKETING/SOCIAL MEDIA")
        elif string == '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, 'TRAILERS', "MARKETING/TRAILERS")
        else: createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, string.upper(), f"MARKETING/{string.upper()}")
        level2_marketing_folderNumber = level2_marketing_folderNumber + 1



def createFolder_level2_custom(level2_custom_parent, relative_template_path):
    clearConsole()
    print(f'''Select needed level 2 folders for {level2_custom_parent}

Type custom folder names (separate by SPACE)''')
    
    level2_custom_selection = input('$ ').split()
    level2_custom_folderNumber = 1

    for string in level2_custom_selection:
        createFolder_level2(level2_custom_parent, level2_custom_folderNumber, string.upper(), relative_template_path)
        level2_custom_folderNumber = level2_custom_folderNumber + 1



def createFolder_level3(parent_level1:str, parent_level2:str, number:int, name:str, relative_template_path:str):
    level3_folder_name = f'{prefix(number)}{name}'
    level3_folder_directory = os.path.join(projectDirectory, parent_level1, parent_level2, level3_folder_name)

    os.mkdir(level3_folder_directory)
    if initfilm.templates.check(relative_template_path) == True:
        initfilm.templates.copy(relative_template_path, level3_folder_directory, level3_folder_name)



def createFolder_level3_raw():
    clearConsole()
    print(f'''Select needer level 3 folders for {level2_folder_name}
    1) A-CAM
    2) B-CAM
    3) C-CAM
    4) D-CAM
    99) SORT LATER

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level3_raw_selection = input('$ ').split()
    level3_raw_folderNumber = 1

    for string in level3_raw_selection:
        if string == '1': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'A-CAM', "FOOTAGE/RAW/A-CAM")
        elif string == '2': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'B-CAM', "FOOTAGE/RAW/B-CAM")
        elif string == '3': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'C-CAM', "FOOTAGE/RAW/C-CAM")
        elif string == '4': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'D-CAM', "FOOTAGE/RAW/D-CAM")
        elif string == '99': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', 99, 'SORT LATER', "FOOTAGE/RAW/SORT LATER")
        else: createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, string.upper(), f"FOOTAGE/RAW/{string.upper()}")
        level3_raw_folderNumber = level3_raw_folderNumber + 1