# Hypster Playlist Downloader

 Command line tool written in python to download a hypster playlist as mp3's. The script first scrapes a hypster playlist url for youtube video links, then rips and converts the audio into mp3 format using the highest quality audio codecs made availble by youtube.

> This is essentially a wrapper around the youtube-dl package developed by [Ricardo Garcia](https://github.com/rg3) 

# Releases

### The latest release can be found ***[here](https://github.com/JarvisPrestidge/hypster-playlist-downloader/releases)***

> If you find you can't run the executable because of missing .DLL errors, then take note of that file name and search online for the associated microsoft c++ runtime library, install this, then try to proceed. (This issue arises since each release binary is compiled with the available .dll's on my computer and those may not align with your system.) 

The best way to fully mitigate this issue is to clone the repo and build the binary yourself using pyinstaller.

* Clone the repo and ensure python 2.x in installed with pip
* Install pyinstaller with - `pip install pyinstaller`
* Then in the root directory run - `pyinstaller.exe --onefile --icon=img/hypster.ico hypster.py`
* This will create a new hypster.exe binary in your /dist folder with the correct .DLLs for your system

# Development

#### Required python pip modules to run the script (hypster.py):
* requests
* youtube-dl
* beautifulsoup4

#### Both the python script and the release executable have hard dependancies on the ffmpeg libraries. As such the following binaries must be availble either on the environent path or in the same working directory as the script during execution:
* ffmpeg.exe
* ffprobe.exe

> These dependancies are packaged into the dist directory of the report but can also be found in the release package.

It may be the case that not all youtube videos are permitted to be viewed (as thus downloaded) in your region. In this case the program will alert you, however won't be able to work around this restriction.

# Example

### Example of the script in action

![Example use](img/script.png?raw=true)

### And the resulting .mp3's in the default download directory

![Example use](img/result.png?raw=true)

Please do let me know about any problems you're having by logging an issue.

Enjoy!