import sys, os



# CREATE PROJECT FOLDER
workingTitle = sys.argv[1]
currentDirectory = os.getcwd()
projectDirectory = os.path.join(currentDirectory, workingTitle)

print(f'Creating project folder for {workingTitle}')

os.mkdir(projectDirectory)



# LEVEL 1 FOLDERS
print(f'''Select needed level 1 folders for {workingTitle}:

    1) PROJECT FILES
    2) ASSETS
    3) FOOTAGE
    4) AUDIO
    5) EXPORT

Type numbers to select or type custom folder names (separate by SPACE)''')
level1Selection = input('$ ').split()
level1FolderNumber = 1
for string in level1Selection:
    if string == '1':
        level1FolderName = str(level1FolderNumber) + '. PROJECT FILES'
        folderDirectory = os.path.join(projectDirectory, level1FolderName)
        os.mkdir(folderDirectory)

        # LEVEL 2 FOLDERS
        print(f'''Select needed level 2 folders for {level1FolderName}:

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
        level2Selection = input('$ ').split()
        level2FolderNumber = 1
        for string in level2Selection:
            if string == '1':
                level2FolderName = str(level2FolderNumber) + '. PREMIERE PRO'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '2':
                level2FolderName = str(level2FolderNumber) + '. DAVINCI RESOLVE'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '3':
                level2FolderName = str(level2FolderNumber) + '. MEDIA COMPOSER'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '4':
                level2FolderName = str(level2FolderNumber) + '. FINAL CUT PRO'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '5':
                level2FolderName = str(level2FolderNumber) + '. SONY VEGAS'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '6':
                level2FolderName = str(level2FolderNumber) + '. HITFILM EXPRESS'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '7':
                level2FolderName = str(level2FolderNumber) + '. AFTER EFFECTS'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '8':
                level2FolderName = str(level2FolderNumber) + '. PHOTOSHOP'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '9':
                level2FolderName = str(level2FolderNumber) + '. ILLUSTRATOR'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '10':
                level2FolderName = str(level2FolderNumber) + '. BLENDER'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '11':
                level2FolderName = str(level2FolderNumber) + '. CINEMA 4D'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '12':
                level2FolderName = str(level2FolderNumber) + '. MAYA'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '13':
                level2FolderName = str(level2FolderNumber) + '. NUKE'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '14':
                level2FolderName = str(level2FolderNumber) + '. HOUDINI'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '15':
                level2FolderName = str(level2FolderNumber) + '. ZBRUSH'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '16':
                level2FolderName = str(level2FolderNumber) + '. AFFINITY DESIGNER'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '17':
                level2FolderName = str(level2FolderNumber) + '. PRO TOOLS'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '18':
                level2FolderName = str(level2FolderNumber) + '. ABLETON'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '19':
                level2FolderName = str(level2FolderNumber) + '. CUBASE'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '20':
                level2FolderName = str(level2FolderNumber) + '. REAPER'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '21':
                level2FolderName = str(level2FolderNumber) + '. IZOTOPE RX'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '22':
                level2FolderName = str(level2FolderNumber) + '. AUDITION'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '23':
                level2FolderName = str(level2FolderNumber) + '. AUDACITY'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '24':
                level2FolderName = str(level2FolderNumber) + '. LOGIC PRO'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '25':
                level2FolderName = str(level2FolderNumber) + '. FL STUDIO'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            level2FolderNumber = level2FolderNumber + 1

    elif string == '2':
        level1FolderName = str(level1FolderNumber) + '. ASSETS'
        folderDirectory = os.path.join(projectDirectory, level1FolderName)
        os.mkdir(folderDirectory)

    elif string == '3':
        level1FolderName = str(level1FolderNumber) + '. FOOTAGE'
        folderDirectory = os.path.join(projectDirectory, level1FolderName)
        os.mkdir(folderDirectory)

        # LEVEL 2 FOLDERS
        print(f'''Select needed level 2 folders for {level1FolderName}:

        1) _graded
        2) _VFX

        Type numbers to select or type custom folder names (separate by SPACE)''')
        level2Selection = input('$ ').split()
        level2FolderNumber = 1
        for string in level2Selection:
            if string == '1':
                level2FolderName = '_graded'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '2':
                level2FolderName = '_VFX'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)

    elif string == '4':
        level1FolderName = str(level1FolderNumber) + '. AUDIO'
        folderDirectory = os.path.join(projectDirectory, level1FolderName)
        os.mkdir(folderDirectory)

        # LEVEL 2 FOLDERS
        print(f'''Select needed level 2 folders for {level1FolderName}:

	1) PFX
	2) SFX
	3) FOLEY
	4) AMBIANCE
	5) MUSIC
	6) SOUNDTRACK
	7) VOICEOVER
    8) ADR

Type numbers to select or type custom folder names (separate by SPACE)''')
        level2Selection = input('$ ').split()
        level2FolderNumber = 1
        for string in level2Selection:
            if string == '1':
                level2FolderName = str(level2FolderNumber) + '. PFX'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '2':
                level2FolderName = str(level2FolderNumber) + '. SFX'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '3':
                level2FolderName = str(level2FolderNumber) + '. FOLEY'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '4':
                level2FolderName = str(level2FolderNumber) + '. AMBIANCE'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '5':
                level2FolderName = str(level2FolderNumber) + '. MUSIC'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '6':
                level2FolderName = str(level2FolderNumber) + '. SOUNDTRACK'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '7':
                level2FolderName = str(level2FolderNumber) + '. VOICEOVER'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '8':
                level2FolderName = str(level2FolderNumber) + '. ADR'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            level2FolderNumber = level2FolderNumber + 1

    elif string == '5':
        level1FolderName = str(level1FolderNumber) + '. EXPORT'
        folderDirectory = os.path.join(projectDirectory, level1FolderName)
        os.mkdir(folderDirectory)

        # LEVEL 2 FOLDERS
        print(f'''Select needed level 2 folders for {level1FolderName}:

	1) PREVIEWS
	2) MASTER
    3) DELIVERABLES

Type numbers to select or type custom folder names (separate by SPACE)''')
        level2Selection = input('$ ').split()
        level2FolderNumber = 1
        for string in level2Selection:
            if string == '1':
                level2FolderName = str(level2FolderNumber) + '. PREVIEWS'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '2':
                level2FolderName = str(level2FolderNumber) + '. MASTER'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            elif string == '3':
                level2FolderName = str(level2FolderNumber) + '. DELIVERABLES'
                folderDirectory = os.path.join(projectDirectory, level1FolderName, level2FolderName)
                os.mkdir(folderDirectory)
            level2FolderNumber = level2FolderNumber + 1

    level1FolderNumber = level1FolderNumber + 1