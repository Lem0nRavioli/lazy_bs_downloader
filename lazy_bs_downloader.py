import requests
import urllib.request
import time
import os

URL_HASH = "https://beatsaver.com/api/maps/by-hash/"
BS_URL = "http://beatsaver.com"
HEADERS = {"User-Agent": "Please/Dont/Block"}

os.makedirs("BeatSong", exist_ok=True)


def download_song(song_url, filename):
    opener = urllib.request.build_opener()
    opener.addheaders = HEADERS.items()
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(song_url, 'BeatSong/' + filename + ".zip")


# categories value for the cat variable
"""
0 = trending
1 = date ranked
2 = scores set
3 = star rating
4 = author
"""
cat = 0
limit = 20  # number of song to download
start = 0  # if already loaded song, define starting point to resume download

# r.json()['songs'][i]['id'] return the song hash to input into the url "https://beatsaver.com/api/maps/by-hash/"
r = requests.get(f"http://scoresaber.com/api.php?function=get-leaderboards&cat={cat}&page=1&limit={limit}")

for song in r.json()['songs'][start:]:
    song_hash = song['id']  # retrieve unique song hash
    direct_dl = requests.get(URL_HASH + song_hash, headers=HEADERS).json()['directDownload']  # retrieve direct dl link
    url_dl = BS_URL + direct_dl  # add direct dl link to https://beatsaver.com
    download_song(url_dl, song_hash)  # download the file
    print(f"Downloading {song['name']} with a rating of {song['stars']}")
    time.sleep(1)  # pause to not overload website
