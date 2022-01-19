from cgi import test
import json
from os import error
import os
import speech_recognition as sr

from num2words import num2words
from subprocess import call
import requests

from Keyword import Keyword

from gtts import gTTS


r = sr.Recognizer()

mic = sr.Microphone()







logfile = open('voice_tests.txt', 'a')

def speak(speech):
        
    myobj = gTTS(text=speech, lang='de', slow=False)
    myobj.save("speech.mp3")
    os.system("mpg321 speech.mp3")


def handle_phrase(self, audio1):
    try:
        text = r.recognize_google(audio1, language="de-DE")
        result_google = f"Online (Google): {text}"
        print("Trying to find Action")
        Keyword.findKeyword(text)
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
