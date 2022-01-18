from os import error
import speech_recognition as sr

from num2words import num2words
from subprocess import call
import requests

r = sr.Recognizer()

mic = sr.Microphone()







logfile = open('voice_tests.txt', 'a')

def speak(speech):
        
    cmd_beg= 'espeak -vde'
    cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
    cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file

    #text = input("Enter the Text: ")
    text = speech
    print(text)

    #Replacing ' ' with '_' to identify words in the text entered
    text = text.replace(' ', '_')

    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+cmd_out+text+cmd_end], shell=True)

def handle_phrase(self, audio1):
    try:
        text = r.recognize_google(audio1, language="de-DE")
        result_google = f"Online (Google): {text}"
        query = {'msg':text}
        response = requests.get('http://127.0.0.1:5000/silentmode', params=query)
        print(response.json())
    except sr.UnknownValueError:
        result_google = "Google Speech didn't recognize anything (UnknownValueError)"
    print(result_google)

    return standardize_voice_results(result_google)


def listen_in_bg():
    def func():
        pass
    try:
        if stop_listening is not None:
            return
    except UnboundLocalError:
        stop_listening = func
        pass
    print("listening...")
    #print('Threshhold: ' + str(r.energy_threshold))
    with mic as source:
        r.adjust_for_ambient_noise(mic, duration=1)

    stop_listening = r.listen_in_background(mic, handle_phrase)

    



def listen():
    
    result_google = ""
    result_sphinx = ""
    print("listening...")
    print('Threshhold: ' + str(r.energy_threshold))
    with mic as source:
        r.adjust_for_ambient_noise(mic, duration=1)
        audio1 = r.listen(source, timeout=5, phrase_time_limit=10)
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
