import os, pyperclip
from . import config, templates, transcode
from .clearconsole import clearConsole



def prefix(number_input:int) -> str:
    """Returns a styled prefix based on the values in the config file.
    Args:
        number_input (int): The prefix number.
    Returns:
        prefix (str): Styled prefix with a number and separator."""

    try:
        visible = config.get("prefix", "visibility")
    except:
        config.set_prefix_visibility("visible")
        visible = config.get("prefix", "visibility")
    number_style = config.get("prefix", "number_style")
    separator_style = config.get("prefix", "separator_style")

    if number_style == "double":
        number_output = f"{number_input:02d}"
    else:
        number_output = number_input
    
    match separator_style:
        case "underscore":
            separator = "_"
        case "parenthesis":
            separator = ") "
        case "space":
            separator = " "
        case _:
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
    if templates.check("") == True:
        templates.copy("", projectDirectory, workingTitle)

    createFolder_level1_project()

    if proxies_footage:
        createProxies()



def createFolder_level1(number:int, name:str):
    global level1_folder_name
    level1_folder_name = f'{prefix(number)}{name}'
    level1_folder_directory = os.path.join(projectDirectory, level1_folder_name)

    os.mkdir(level1_folder_directory)
    if templates.check(name) == True:
        templates.copy(name, level1_folder_directory, level1_folder_name)



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
        match string:
            case '1':
                createFolder_level1(level1_project_folderNumber, 'PROJECT FILES')
                createFolder_level2_projectFiles()
            case '2':
                createFolder_level1(level1_project_folderNumber, 'ASSETS')
                createFolder_level2_assets()
            case '3':
                createFolder_level1(level1_project_folderNumber, 'FOOTAGE')
                createFolder_level2_footage()
            case '4':
                createFolder_level1(level1_project_folderNumber, 'AUDIO')
                createFolder_level2_audio()
            case '5':
                createFolder_level1(level1_project_folderNumber, 'EXPORT')
                createFolder_level2_export()
            case '6':
                createFolder_level1(level1_project_folderNumber, 'DOCUMENTS')
                createFolder_level2_documents()
            case '7':
                createFolder_level1(level1_project_folderNumber, 'MARKETING')
                createFolder_level2_marketing()
            case _:
                createFolder_level1(level1_project_folderNumber, string.upper())
                createFolder_level2_custom(f'{prefix(level1_project_folderNumber)}{string.upper()}', string.upper())
        level1_project_folderNumber = level1_project_folderNumber + 1



def createFolder_level2(parent:str, number:int, name:str, relative_template_path:str):
    global level2_folder_name
    level2_folder_name = f'{prefix(number)}{name}'
    level2_folder_directory = os.path.join(projectDirectory, parent, level2_folder_name)

    os.mkdir(level2_folder_directory)
    if templates.check(relative_template_path) == True:
        templates.copy(relative_template_path, level2_folder_directory, level2_folder_name)



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
        match string:
            case '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'PREMIERE PRO', "PROJECT FILES/PREMIERE PRO")
            case '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'DAVINCI RESOLVE', "PROJECT FILES/DAVINCI RESOLVE")
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'MEDIA COMPOSER', "PROJECT FILES/MEDIA COMPOSER")
            case '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'FINAL CUT PRO', "PROJECT FILES/FINAL CUT PRO")
            case '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'SONY VEGAS', "PROJECT FILES/SONY VEGAS")
            case '6': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'HITFILM EXPRESS', "PROJECT FILES/HITFILM EXPRESS")
            case '7': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AFTER EFFECT', "PROJECT FILES/AFTER EFFECTS")
            case '8': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'PHOTOSHOP', "PROJECT FILES/PHOTOSHOP")
            case '9': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'ILLUSTRATOR', "PROJECT FILES/ILLUSTRATOR")
            case '10': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'BLENDER', "PROJECT FILES/BLENDER")
            case '11': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'CINEMA 4D', "PROJECT FILES/CINEMA 4D")
            case '12': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'MAYA', "PROJECT FILES/MAYA")
            case '13': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'NUKE', "PROJECT FILES/NUKE")
            case '14': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'HOUDINI', "PROJECT FILES/HOUDINI")
            case '15': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'ZBRUSH', "PROJECT FILES/ZBRUSH")
            case '16': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AFFINITY DESIGNER', "PROJECT FILES/AFFINITY DESIGNER")
            case '17': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'PRO TOOLS', "PROJECT FILES/PRO TOOLS")
            case '18': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'ABLETON', "PROJECT FILES/ABLETON")
            case '19': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'CUBASE', "PROJECT FILES/CUBASE")
            case '20': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'REAPER', "PROJECT FILES/REAPER")
            case '21': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'IZOTOPE RX', "PROJECT FILES/IZOTOPE RX")
            case '22': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AUDITION', "PROJECT FILES/AUDITION")
            case '23': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'AUDACITY', "PROJECT FILES/AUDACITY")
            case '24': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'LOGIC PRO', "PROJECT FILES/LOGIC PRO")
            case '25': createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, 'FL STUDIO', "PROJECT FILES/FL STUDIO")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}PROJECT FILES', level2_projectFiles_folderNumber, string.upper(), f"PROJECT FILES/{string.upper()}")
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
        match string:
            case '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'LOGOS', "ASSETS/LOGOS")
            case '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'GRAPHICS', "ASSETS/GRAPHICS")
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'FONTS', "ASSETS/FONTS")
            case '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'OVERLAYS', "ASSETS/OVERLAYS")
            case '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, 'REFERENCE', "ASSETS/REFERENCE")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}ASSETS', level2_assets_folderNumber, string.upper(), f"ASSETS/{string.upper()}")
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
    global level2_footage_folderNumber, proxies_footage
    level2_footage_folderNumber = 1
    proxies_footage = None

    for string in level2_footage_selection:
        match string:
            case '1':
                createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'RAW', "FOOTAGE/RAW")
                createFolder_level3_raw()
            case '2':
                createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'PROXIES', "FOOTAGE/PROXIES")
                proxies_footage = f'{prefix(level1_project_folderNumber)}FOOTAGE'
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'STOCK', "FOOTAGE/STOCK")
            case '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'VFX', "FOOTAGE/VFX")
            case '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, 'GRADED', "FOOTAGE/GRADED")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}FOOTAGE', level2_footage_folderNumber, string.upper(), f"FOOTAGE/{string.upper()}")
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
        match string:
            case '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'PFX', "AUDIO/PFX")
            case '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'SFX', "AUDIO/SFX")
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'FOLEY', "AUDIO/FOLEY")
            case '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'AMBIANCE', "AUDIO/AMBIANCE")
            case '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'MUSIC', "AUDIO/MUSIC")
            case '6': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'SOUNDTRACK', "AUDIO/SOUNDTRACK")
            case '7': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'VOICEOVER', "AUDIO/VOICEOVER")
            case '8': createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_folderNumber, 'ADR', "AUDIO/ADR")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}AUDIO', level2_audio_selection, string.upper(), f"AUDIO/{string.upper()}")
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
        match string:
            case '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, 'PREVIEWS', "EXPORT/PREVIEWS")
            case '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, 'MASTER', "EXPORT/MASTER")
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, 'DELIVERABLES', "EXPORT/DELIVERABLES")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}EXPORT', level2_export_folderNumber, string.upper(), f"EXPORT/{string.upper()}")
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
        match string:
            case '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'NOTES', "DOCUMENTS/NOTES")
            case '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'MOODBOARD', "DOCUMENTS/MOODBOARD")
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'STORYBOARD', "DOCUMENTS/STORYBOARD")
            case '4': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'SCRIPT', "DOCUMENTS/SCRIPT")
            case '5': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'PITCH', "DOCUMENTS/PITCH")
            case '6': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'LEGAL', "DOCUMENTS/LEGAL")
            case '7': createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, 'FINANCIAL', "DOCUMENTS/FINANCIAL")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}DOCUMENTS', level2_documents_folderNumber, string.upper(), f"DOCUMENTS/{string.upper()}")
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
        match string:
            case '1': createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, 'POSTERS', "MARKETING/POSTERS")
            case '2': createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, 'SOCIAL MEDIA', "MARKETING/SOCIAL MEDIA")
            case '3': createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, 'TRAILERS', "MARKETING/TRAILERS")
            case _: createFolder_level2(f'{prefix(level1_project_folderNumber)}MARKETING', level2_marketing_folderNumber, string.upper(), f"MARKETING/{string.upper()}")
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
    if templates.check(relative_template_path) == True:
        templates.copy(relative_template_path, level3_folder_directory, level3_folder_name)



def createFolder_level3_raw():
    clearConsole()
    print(f'''Select needed level 3 folders for {level2_folder_name}

    1) A-CAM
    2) B-CAM
    3) C-CAM
    4) D-CAM
    99) SORT LATER

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level3_raw_selection = input('$ ').split()
    level3_raw_folderNumber = 1

    for string in level3_raw_selection:
        match string:
            case '1': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'A-CAM', "FOOTAGE/RAW/A-CAM")
            case '2': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'B-CAM', "FOOTAGE/RAW/B-CAM")
            case '3': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'C-CAM', "FOOTAGE/RAW/C-CAM")
            case '4': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, 'D-CAM', "FOOTAGE/RAW/D-CAM")
            case '99': createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', 99, 'SORT LATER', "FOOTAGE/RAW/SORT LATER")
            case _: createFolder_level3(f'{prefix(level1_project_folderNumber)}FOOTAGE', f'{prefix(level2_footage_folderNumber)}RAW', level3_raw_folderNumber, string.upper(), f"FOOTAGE/RAW/{string.upper()}")
        level3_raw_folderNumber = level3_raw_folderNumber + 1



def createProxies():
    """Ask user to make proxies & input codec and resolution. Transcode footage."""

    clearConsole()
    print('Would you like to create proxies for RAW footage? (Y/n)\n(You can always do this later! See --help)')
    transcode_selection = input('$ ')
    if transcode_selection == 'n':
        print('Skipping proxy creation.')
    
    else:
        clearConsole()
        print(f'Select codec (supported: h264, dnxhr, prores-proxy, prores-lt):')
        codec_selection = input('$ ')
        if codec_selection:
            codec = codec_selection
        else:
            codec = 'h264'

        clearConsole()
        print(f'Select resolution (ex. 1280x720):')
        resolution_selection = input('$ ')
        if resolution_selection:
            resolution = resolution_selection
        else:
            resolution = '1280x720'
        
        transcode.transcode_footage(os.path.join(projectDirectory, proxies_footage), codec, resolution)