# Jarvis Prestidge: BeautifulSoup web-scraping script
# Description:		Download hypster.com playlist in .mp3

from __future__ import unicode_literals
from bs4 import BeautifulSoup

import os
import youtube_dl
import requests

print("\nWelcome to the hypster playlist downloader.\n"
      "\nAll songs will be ripped using the highest quality audio codecs"
      "\nmade availble by youtube and converted to mp3. Simply follow the"
      "\ntext based prompts below and enjoy!")

print("\n================================================================")

while True:
    url = raw_input("\nEnter valid hypster playlist url: ")
    domain = "hypster.com/playlists/"
    try:
        realUrl = requests.get(url).status_code
    except requests.exceptions.RequestException as ex:
        print("\nInvalid url entered... please try again.")
        continue
    if realUrl == 200 and url.find(domain) > -1:
        print("\nAccepted!")
        break
    print("\nInvalid url entered... please try again.")

print("\n================================================================")

while True:
    isPath = raw_input("\nWould you like to specify a "
                       "download directory? (y/n) ")
    if isPath == 'y':
        print("\nTips: 1. Copy & paste path from windows explorer."
              "\n      2. Leave trailing \"\\\" after last folder name. ")
        path = raw_input("\nEnter valid full path for download directory: ")
        if len(path) > 0:
            if path[-1:] != '\\':
                path += '\\'
            if os.path.isdir(path):
                print("\nAccepted!")
                break
        else:
            print("\nPath does not exist... please try again.")
    elif isPath == 'n':
        path = os.environ.get('USERPROFILE') + \
            "\\Downloads\\hypster-playlist\\"
        if not os.path.exists(path):
            os.makedirs(path)
        print("\nUsing default windows download directory: " + path)
        break
    else:
        print("\nPlease enter either <y> or <n> only.")

print("\n================================================================")

print("\nCommencing download of playlist, this may take some time...\n")

# Making the http request
result = requests.get(url)

# Getting content from request
content = result.content

# Parsing the content using the default python html parser
soup = BeautifulSoup(content, "html.parser")

# Scraping all the required tags into list
soupLst = soup.find_all("div", "songPLB")

# List comprehension, string conversion, substring
linkLst = [str(div)[40:51] for div in soupLst]

# Youtube converter api string declaration
titleUrl = ("http://www.youtubeinmp3.com/fetch/?format=text"
            "&video=http://www.youtube.com/watch?v=")

musicUrl = ("http://www.youtubeinmp3.com/fetch/?"
            "video=https://www.youtube.com/watch?v=")

ytdl_opts = {
    'outtmpl': path + '%(title)s.%(ext)s',
    'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
}

for link in linkLst:

    # Download the song with the given dir & name
    try:
        # Calling youtube-dl with the ytdl_opt dict
        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
            # Downloading the audio
            ytdl.download([link])
    except youtube_dl.utils.DownloadError:
        print("Video is not available in your region... skipping to next.")
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex), ex.args)
        print(message)

print("\n================================================================")

print("\nSuccessfully downloaded {0} songs to {1}".format(len(linkLst), path))

print("\nExiting...")

raise SystemExit
