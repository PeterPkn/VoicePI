import Backend.Commands.Music as music
import Backend.Voice.Voice as voice
import Backend.Commands.Weather as weather

standardized_voice = voice.listen()
if standardized_voice["key"] == "play":
    url = music.find_url(f"{standardized_voice['query']} music")
    print(f"Query: {standardized_voice['query']}")
    print(url)
    music.play_video(url)

