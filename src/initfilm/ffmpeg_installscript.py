# Copyright (C) 2025  Andreas Delabie

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



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
        print('Are you using Apple Silicon (M1,M2,M3,...) or Intel?')
        match input('(silicon/intel)$ '):
            case 'silicon':
                subprocess.call('curl -O https://www.osxexperts.net/ffmpeg711arm.zip', shell=True)
                subprocess.call('sudo unzip ffmpeg711arm.zip -d /opt/ffmpeg', shell=True)
            case 'intel':
                subprocess.call('curl -O https://www.osxexperts.net/ffmpeg71intel.zip', shell=True)
                subprocess.call('sudo unzip ffmpeg71intel.zip -d /opt/ffmpeg', shell=True)
        subprocess.call('echo "/opt/ffmpeg" | sudo tee -a /etc/paths', shell=True)
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