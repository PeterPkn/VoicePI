import speech_recognition as sr
# unter Windows: pip install pipwin --> dann "pipwin install pocketsphinx"
import pocketsphinx

r = sr.Recognizer()

"""sound = sr.AudioFile('testsound.wav')
with sound as source:
    audio = r.record(source)"""

"""print("Offline Audio Test 1: ")
print(r.recognize_sphinx(audio))
print("Offline Audio Test 2: ")
print(r.recognize_sphinx(audio))
print("Offline Audio Test 3: ")
print(r.recognize_sphinx(audio))
print("Offline Audio Test 4: ")
print(r.recognize_sphinx(audio))"""

# print("Online Audio Test 1:")
# print(r.recognize_google(audio))


mic = sr.Microphone()
#   with mic as source:
#       audio1 = r.listen(source)

#   print(type(audio1))
while True:
    print("listening...")
    with mic as source:
        audio1 = r.listen(source)

    #   print(type(audio1))
    try:
        print("Online (Google): " + r.recognize_google(audio1, language="de-DE"))
    except sr.UnknownValueError:
        print("Google Speech didn't recognize anything (UnknownValueError)")

    try:
        print("Offline (Sphinx): " + r.recognize_sphinx(audio1))
    except sr.UnknownValueError:
        print("Pocketsphinx didn't recognize anything (UnknownValueError)")

#   if there is no standard mic:
#   print(sr.Microphone.list_microphone_names())
#   mic = sr.Microphone(device_index=2)
