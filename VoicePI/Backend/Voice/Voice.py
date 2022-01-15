import speech_recognition as sr


r = sr.Recognizer()

mic = sr.Microphone()

logfile = open('voice_tests.txt', 'a')


def listen():
    r.adjust_for_ambient_noise(mic, duration=5)
    result_google = ""
    result_sphinx = ""
    print("listening...")
    with mic as source:
        audio1 = r.listen(source)
    print("listening finished")
        #   print(type(audio1))
    print("attempting google")
    try:
        text = r.recognize_google(audio1, language="de-DE")
        result_google = f"Online (Google): {text}"
    except sr.UnknownValueError:
        result_google = "Google Speech didn't recognize anything (UnknownValueError)"
    print(result_google)

    return standardize_voice_results(result_google)


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
"""
    print("attempting sphinx")
    try:
        text = r.recognize_sphinx(audio1, )
        print(text)
        result_sphinx = f"Offline (Sphinx): {text}"
    except sr.UnknownValueError:
        result_sphinx = "Pocketsphinx didn't recognize anything (UnknownValueError)"
    print(result_sphinx)

    result = f"{result_google}\n\n{result_sphinx}\n------------------------------\n\n"
    logfile.write(result)
    return result
"""

# print(listen())
