from logging import error
from threading import Thread
import pafy, vlc, time
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup

from ThreadManager import ThreadManager

th = ThreadManager()


def find_url(name):
        query_string = urllib.parse.urlencode({"search_query": name})
        format_url = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        search_results = re.findall(r"watch\?v=(\S{11})", format_url.read().decode())
        try:
            clip = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        except error:
            return 'No CLIP found'
        print(clip)
        return clip

class MusicPlayer:


        
    def __init__(self, name):
        self.url = find_url(name)
        self._running = True
        
    
    def terminate(self):
        print("User requested STOP")
        self._running = False
    
    def start(self):
        th.AddMusicThread(self.play_video, (), self.terminate)

    def getMetadata(self):
        try:
            video = pafy.new(self.url)
            duration = video.duration
            print(f"Metadata: \n{video}")    
            return [video.title, video.author]
        except KeyError as error:
            print("KeyError, Trying again")
            print(error.with_traceback)
            video = None
        except URLError as error:
            print("URL Error, Probaby no Internet Connection")
            print(error.with_traceback)


    def play_video(self):
        
        #print(f"url: {self.url}")
        video = None
        while video is None and self._running:
            try:
                print("MUSIC??")
                video = pafy.new(self.url)
                print("MUSIC??...")
                print(f"Metadata: \n{video}")
                #pass_infos=[video.title, video.author]
            except KeyError as error:
                print("KeyError, Trying again")
                print(error.with_traceback)

                video = None
            except URLError as error:
                print("URL Error, Probaby no Internet Connection")
                print(error.with_traceback)

        # ftr = [3600, 60, 1]
        # duration = sum([a * b for a, b in zip(ftr, map(int, duration.split(':')))])
        print(f"Video: {video}")
        best = video.getbestaudio()
        playurl = best.url
        print(f"Real-URL: {playurl}")

        Instance = vlc.Instance("-I dummy --no-video --aout=alsa")
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()

        player.set_media(Media)
        player.play()

        time.sleep(10)
        while player.is_playing() == 1 and self._running:
            pass
            #   print(player.is_playing())

        print("stopping player")
        player.stop()


    #urli = find_url("AMOGUS reapster")
    #urli = find_url("Radetzkymarsch")
    #urli = find_url("the Star treks monologue")
    #urli = find_url("ospf lyric")

    #play_video(urli)
