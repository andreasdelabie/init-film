import platform, subprocess



def detectOS() -> str:
    match platform.system():
        case 'Windows':
            return 'windows'
        case 'Darwin':
            return 'mac'
        case _:
            print("We haven't detected a Windows or MacOS operating system, so we suspect you are using Linux.\nWhat's your distro based on?")
            platform_linux = input('(debian/arch/fedora)$ ')
            if platform_linux.lower() not in ['debian', 'arch', 'fedora']:
                print("We need to know if your distro is based on Debian, Arch or Fedora to install FFmpeg correctly.\nIf you know what you're doing you can always install FFmpeg manually through your distro's package manager!")
                exit(1)
            return platform_linux.lower()



def install_windows():
    try:
        subprocess.call('winget install ffmpeg')
    except Exception as e:
        print(f"An error occurred while trying to install FFmpeg on Windows: {e}")



def install_mac():
    try:
        subprocess.call(['/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                         'brew install ffmpeg'])
    except Exception as e:
        print(f"An error occurred while trying to install FFmpeg on MacOS: {e}")



def install_linux(distro: str):
    try:
        match distro:
            case 'debian':
                subprocess.call('sudo apt install ffmpeg')
            case 'arch':
                subprocess.call('sudo pacman -S ffmpeg')
            case 'fedora':
                subprocess.call('sudo dnf install ffmpeg')
    except Exception as e:
        print(f"An error occurred while trying to install FFmpeg on Linux: {e}")



def main():
    try:
        subprocess.call('ffmpeg -version', stdout=subprocess.DEVNULL)
        print("FFmpeg is already installed.")
    except:
        system_os = detectOS()
        match system_os:
            case 'windows':
                install_windows()
            case 'mac':
                install_mac()
            case 'debian':
                install_linux('debian')
            case 'arch':
                install_linux('arch')
            case 'fedora':
                install_linux('fedora')
        print("FFmpeg installation complete. You can now use it with Init-Film.")