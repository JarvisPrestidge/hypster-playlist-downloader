# Hypster Playlist Downloader

 Command line tool written in python to download a hypster playlist as mp3's. The script first scrapes a hypster playlist url for youtube video links, then rips and converts the audio into mp3 format using the highest quality audio codecs made availble by youtube.

> This is essentially a wrapper around the youtube-dl package developed by [Ricardo Garcia](https://github.com/rg3) 

### The release can be found here

#### Required python pip modules to run the script (hypster.py):
* requests
* youtube-dl
* beautifulsoup4

#### Both the python script and the release executable have hard dependancies on the ffmpeg libraries. As such the following binaries must be availble either on the environent path or in the same working directory as the script during execution:
* ffmpeg.exe
* ffprobe.exe

> These dependancies are packaged into the bin directory of the current release but can also be found in the lib folder of the repo

It may be the case that not all youtube videos are permitted to be viewed (as thus downloaded) in your region. In this case the program will alert you, however won't be able to work around this restriction.

Example of the script in action:

![Example use](/screenshot.png?raw=true)
