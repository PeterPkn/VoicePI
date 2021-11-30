import Backend.Commands.Music as music
import Backend.Voice.Voice as voice


def standardize_voice_results(voice_data):
    data = {"key": "", "query": ""}
    keylist_play = ["spiel", "spiele", "play"]
    keylist_show = ["zeig", "zeige", "show"]
    keylist = keylist_show + keylist_play

    for key in keylist:
        if key in voice_data:
            data["key"] = "play"
            query = ""
            for item in voice_data[voice_data.index(key):]:
                query += f" {item}"

            data["query"] = query

    return data


voice_result = voice.listen().lower().split(" ")
print(voice_result)
standardized_voice = standardize_voice_results(voice_result)
if standardized_voice["key"] == "play":
    url = music.find_url(f"{standardized_voice['query']} music")
    print(f"Query: {standardized_voice['query']}")
    print(url)
    music.play_video(url)

