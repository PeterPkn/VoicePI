import imp
import pafy, vlc, time
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import Searchengine


def play_video(url):
    print("play_video")
    print(f"url: {url}")
    video = None
    while video is None:
        try:
            video = pafy.new(url)
            print(f"Metadata: \n{video}")
        except KeyError:
            print("KeyError, Trying again")
            video = None

    # ftr = [3600, 60, 1]
    # duration = sum([a * b for a, b in zip(ftr, map(int, duration.split(':')))])
    print(f"Video: {video}")
    best = video.getbest()
    playurl = best.url
    print(f"Real-URL: {playurl}")

    Instance = vlc.Instance("-I dummy --no-video --aout=alsa --file-logging --logfile=vlc-log.txt --verbose 3")
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()

    player.set_media(Media)
    player.play()

    time.sleep(10)
    while player.is_playing() == 1:
        pass
        #   print(player.is_playing())

    print("stopping player")
    player.stop()


#urli = find_url("AMOGUS reapster")
#urli = find_url("Radetzkymarsch")
#urli = find_url("the Star treks monologue")
urli = Searchengine.find_url("white friday sabaton")

play_video(urli)
