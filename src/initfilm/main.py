import os



def clearConsole():
    osname = os.name
    if osname == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For macOS & Linux



def createFolder_level0():
    global projectDirectory, workingTitle

    clearConsole()
    print('Enter project name:')

    workingTitle = input('$ ')
    currentDirectory = os.getcwd()
    projectDirectory = os.path.join(currentDirectory, workingTitle)

    os.mkdir(projectDirectory)

    createFolder_level1_project()



def createFolder_level1(number, name):
    level1_folder_name = f'{str(number)}. {name}'
    level1_folder_directory = os.path.join(projectDirectory, level1_folder_name)

    os.mkdir(level1_folder_directory)



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
            createFolder_level2_custom(f'{str(level1_project_folderNumber)}. ' + string.upper())
        level1_project_folderNumber = level1_project_folderNumber + 1



def createFolder_level2(parent, number, name):
    level2_folder_name = f'{str(number)}. {name}'
    level2_folder_directory = os.path.join(projectDirectory, parent, level2_folder_name)

    os.mkdir(level2_folder_directory)



def createFolder_level2_projectFiles():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. PROJECT FILES:

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
    global level2_projectFiles_folderNumber
    level2_projectFiles_folderNumber = 1

    for string in level2_projectFiles_selection:
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'PREMIERE PRO')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'DAVINCI RESOLVE')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'MEDIA COMPOSER')
        elif string == '4': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'FINAL CUT PRO')
        elif string == '5': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'SONY VEGAS')
        elif string == '6': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'HITFILM EXPRESS')
        elif string == '7': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'AFTER EFFECT')
        elif string == '8': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'PHOTOSHOP')
        elif string == '9': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'ILLUSTRATOR')
        elif string == '10': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'BLENDER')
        elif string == '11': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'CINEMA 4D')
        elif string == '12': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'MAYA')
        elif string == '13': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'NUKE')
        elif string == '14': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'HOUDINI')
        elif string == '15': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'ZBRUSH')
        elif string == '16': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'AFFINITY DESIGNER')
        elif string == '17': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'PRO TOOLS')
        elif string == '18': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'ABLETON')
        elif string == '19': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'CUBASE')
        elif string == '20': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'REAPER')
        elif string == '21': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'IZOTOPE RX')
        elif string == '22': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'AUDITION')
        elif string == '23': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'AUDACITY')
        elif string == '24': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'LOGIC PRO')
        elif string == '25': createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, 'FL STUDIO')
        else: createFolder_level2(f'{level1_project_folderNumber}. PROJECT FILES', level2_projectFiles_folderNumber, string.upper())
        level2_projectFiles_folderNumber = level2_projectFiles_folderNumber + 1



def createFolder_level2_assets():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. ASSETS

    1. LOGOS
    2. GRAPHICS
    3. FONTS
    4. OVERLAYS
    5. REFERENCE

Type custom folder names (separate by SPACE)''')

    level2_assets_selection = input('$ ').split()
    global level2_assets_folderNumber
    level2_assets_folderNumber = 1

    for string in level2_assets_selection:
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. ASSETS', level2_assets_folderNumber, 'LOGOS')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. ASSETS', level2_assets_folderNumber, 'GRAPHICS')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. ASSETS', level2_assets_folderNumber, 'FONTS')
        elif string == '4': createFolder_level2(f'{level1_project_folderNumber}. ASSETS', level2_assets_folderNumber, 'OVERLAYS')
        elif string == '5': createFolder_level2(f'{level1_project_folderNumber}. ASSETS', level2_assets_folderNumber, 'REFERENCE')
        else: createFolder_level2(f'{level1_project_folderNumber}. ASSETS', level2_assets_folderNumber, string.upper())
        level2_assets_folderNumber = level2_assets_folderNumber + 1



def createFolder_level2_footage():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. FOOTAGE
    
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
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. FOOTAGE', level2_footage_folderNumber, 'RAW')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. FOOTAGE', level2_footage_folderNumber, 'PROXIES')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. FOOTAGE', level2_footage_folderNumber, 'STOCK')
        elif string == '4': createFolder_level2(f'{level1_project_folderNumber}. FOOTAGE', level2_footage_folderNumber, 'VFX')
        elif string == '5': createFolder_level2(f'{level1_project_folderNumber}. FOOTAGE', level2_footage_folderNumber, 'GRADED')
        else: createFolder_level2(f'{level1_project_folderNumber}. FOOTAGE', level2_footage_folderNumber, string.upper())
        level2_footage_folderNumber = level2_footage_folderNumber + 1



def createFolder_level2_audio():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. AUDIO

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
    global level2_audio_folderNumber
    level2_audio_folderNumber = 1

    for string in level2_audio_selection:
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'PFX')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'SFX')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'FOLEY')
        elif string == '4': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'AMBIANCE')
        elif string == '5': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'MUSIC')
        elif string == '6': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'SOUNDTRACK')
        elif string == '7': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'VOICEOVER')
        elif string == '8': createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_folderNumber, 'ADR')
        else: createFolder_level2(f'{level1_project_folderNumber}. AUDIO', level2_audio_selection, string.upper())
        level2_audio_folderNumber = level2_audio_folderNumber + 1



def createFolder_level2_export():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. EXPORT

    1) PREVIEWS
    2) MASTER
    3) DELIVERABLES

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_export_selection = input('$ ').split()
    global level2_export_folderNumber
    level2_export_folderNumber = 1

    for string in level2_export_selection:
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. EXPORT', level2_export_folderNumber, 'PREVIEWS')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. EXPORT', level2_export_folderNumber, 'MASTER')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. EXPORT', level2_export_folderNumber, 'DELIVERABLES')
        else: createFolder_level2(f'{level1_project_folderNumber}. EXPORT', level2_export_folderNumber, string.upper())
        level2_export_folderNumber = level2_export_folderNumber + 1



def createFolder_level2_documents():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. DOCUMENTS
    
    1) MOODBOARD
    2) STORYBOARD
    3) SCRIPT
    4) LEGAL
    5) FINANCIAL

Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_documents_selection = input('$ ').split()
    global level2_documents_folderNumber
    level2_documents_folderNumber = 1

    for string in level2_documents_selection:
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. DOCUMENTS', level2_documents_folderNumber, 'MOODBOARD')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. DOCUMENTS', level2_documents_folderNumber, 'STORYBOARD')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. DOCUMENTS', level2_documents_folderNumber, 'SCRIPT')
        elif string == '4': createFolder_level2(f'{level1_project_folderNumber}. DOCUMENTS', level2_documents_folderNumber, 'LEGAL')
        elif string == '5': createFolder_level2(f'{level1_project_folderNumber}. DOCUMENTS', level2_documents_folderNumber, 'FINANCIAL')
        else: createFolder_level2(f'{level1_project_folderNumber}. DOCUMENTS', level2_documents_folderNumber, string.upper())
        level2_documents_folderNumber = level2_documents_folderNumber + 1



def createFolder_level2_marketing():
    clearConsole()
    print(f'''Select needed level 2 folders for {level1_project_folderNumber}. MARKETING
    
    1) POSTERS
    2) SOCIAL MEDIA
    3) TRAILERS
    
Type numbers to select or type custom folder names (separate by SPACE)''')
    
    level2_marketing_selection = input('$ ').split()
    global level2_marketing_folderNumber
    level2_marketing_folderNumber = 1

    for string in level2_marketing_selection:
        if string == '1': createFolder_level2(f'{level1_project_folderNumber}. MARKETING', level2_marketing_folderNumber, 'POSTERS')
        elif string == '2': createFolder_level2(f'{level1_project_folderNumber}. MARKETING', level2_marketing_folderNumber, 'SOCIAL MEDIA')
        elif string == '3': createFolder_level2(f'{level1_project_folderNumber}. MARKETING', level2_marketing_folderNumber, 'TRAILERS')
        else: createFolder_level2(f'{level1_project_folderNumber}. MARKETING', level2_marketing_folderNumber, string.upper())
        level2_marketing_folderNumber = level2_marketing_folderNumber + 1



def createFolder_level2_custom(level2_custom_parent):
    clearConsole()
    print(f'''Select needed level 2 folders for {level2_custom_parent}

Type custom folder names (separate by SPACE)''')
    
    level2_custom_selection = input('$ ').split()
    global level2_custom_folderNumber
    level2_custom_folderNumber = 1

    for string in level2_custom_selection:
        createFolder_level2(level2_custom_parent, level2_custom_folderNumber, string.upper())
        level2_custom_folderNumber = level2_custom_folderNumber + 1