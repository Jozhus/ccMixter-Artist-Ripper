import urllib.request, os
from bs4 import BeautifulSoup

def getHTML(offset = 0):
    global profile
    url = "http://ccmixter.org/people/" + profile + "/?offset=" + str(offset)
    html = urllib.request.urlopen(url)
    html = BeautifulSoup(html, 'html.parser')
    return html

def getSongs(html):
    offset = 0
    songs = []
    while 1:
        foundsongs = getHTML(offset).find_all('div', 'upload_info')
        if len(foundsongs) == 0:
            break
        songs += [x['about'] for x in foundsongs]
        offset += 15
    return songs

def download(songs):
    global profile
    path = "ccMixter/" + profile
    if not os.path.exists(path):
        os.makedirs(path)
    for song in songs:
        songname = song.split(profile + "_%2D_")[1].replace('_', ' ')
        if not os.path.isfile(path + '/' + songname):
            print("Downloading " + songname)
            urllib.request.urlretrieve(song, path + '/' + songname)

profile = input("Profile: ")
download(getSongs(getHTML()))
print("Done!")
