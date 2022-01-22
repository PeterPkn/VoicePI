from logging import error
from threading import Thread
import pafy, vlc, time
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup

from ThreadManager import ThreadManager

th = ThreadManager()

#TODO: Rewrite to Class

def find_url(name):
        query_string = urllib.parse.urlencode({"search_query": name})
        format_url = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        search_results = re.findall(r"watch\?v=(\S{11})", format_url.read().decode())
        clip = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

        print(clip)
        return clip

class VideoPlayer:


        
    def __init__(self, name):
        self.url = find_url(name)
        self._running = True
        
    
    def terminate(self):
        print("User requested STOP")
        self._running = False
    
    def start(self):
        th.AddVideoThread(self.play_video, (), self.terminate)

    def getMetadata(self):
        try:
            pafy.dump_cache()
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
        #print("play_video")
        #print(f"url: {self.url}")
        video = None
        while video is None and self._running:
            try:
                video = pafy.new(self.url)
                duration = video.duration
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
        best = video.getbest()
        playurl = best.url
        print(f"Real-URL: {playurl}")

        Instance = vlc.Instance("-I dummy --aout=alsa")
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()

        player.set_media(Media)
        player.toggle_fullscreen()
        player.play()

        time.sleep(10)
        while player.is_playing() == 1 and self._running:
            pass
            #   print(player.is_playing())

        print("stopping player")
        player.stop()
