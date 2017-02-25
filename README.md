# Hypster Playlist Downloader

 Command line tool written in python to download a hypster playlist as mp3's. The script first scrapes a hypster playlist url for youtube video links, then rips and converts the audio into mp3 format using the highest quality audio codecs made availble by youtube.

> This is essentially a wrapper around the youtube-dl package developed by [Ricardo Garcia](https://github.com/rg3) 

#### Required packages to run the script:
* requests
* youtube-dl
* beautifulsoup4

#### The script has hard dependancies on FFmpeg, as such it requires the following binaries to be availble either on the path or in the same working directory as the script during execution:
* ffmpeg.exe
* ffprobe.exe

> These dependancies are packaged in the bin directory of the current release which can be found ***[here]()***

It may be the case that not all youtube videos are permitted to be viewed (as thus downloaded) in your region. In this case the program will alert you, however won't be able to work around this restriction.

Example of the script in action:

![Example use](/screenshot.png?raw=true)
