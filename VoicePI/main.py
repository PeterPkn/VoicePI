import Backend.Commands.Music as music
import Backend.Voice.Voice as voice

voice_result = voice.listen().lower().split(" ")
print(voice_result)

if any(x in ["spiel", "spiele"] for x in voice_result):
    url = music.find_url(voice_result[1])
    print(url)
    music.play_video(url)
