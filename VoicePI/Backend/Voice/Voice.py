from time import sleep
import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone()
logfile = open('voice_tests.txt', 'a')


def handle_phrase(self, audio1):
    try:
        text = r.recognize_google(audio1, language="de-DE")
        result_google = f"Online (Google): {text}"
    except sr.UnknownValueError:
        result_google = "Google Speech didn't recognize anything (UnknownValueError)"
    print(result_google)

    return standardize_voice_results(result_google)


def listen_in_bg():
    print("listening...")
    #print('Threshhold: ' + str(r.energy_threshold))
    with mic as source:
        r.adjust_for_ambient_noise(mic, duration=1)

    stop_listening = r.listen_in_background(mic, handle_phrase)

    sleep(30)

    stop_listening()


def standardize_voice_results(voice_data):
    voice_data = voice_data.lower().split(" ")
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


# print(listen())
listen_in_bg()
