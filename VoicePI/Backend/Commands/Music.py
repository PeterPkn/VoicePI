import pafy, vlc

try:
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    print(playurl)

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    print(Media)
    print(player)
    while True:
        player.play()
except KeyError:
    print("dIsLiKeCoUnT")
