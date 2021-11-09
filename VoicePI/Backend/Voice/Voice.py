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

testfile = open('voice_tests.txt', 'a')

"""
while True:
    print("listening...")
    with mic as source:
        audio1 = r.listen(source)

    #   print(type(audio1))
    try:
        text = r.recognize_google(audio1, language="de-DE")
        result_google = f"Online (Google): {text}"
    except sr.UnknownValueError:
        result_google = "Google Speech didn't recognize anything (UnknownValueError)"

    try:
        text = r.recognize_sphinx(audio1)
        result_sphinx = f"Offline (Sphinx): {text}"
    except sr.UnknownValueError:
        result_sphinx = "Pocketsphinx didn't recognize anything (UnknownValueError)"

    testfile.write(f"{result_google}\n\n{result_sphinx}\n------------------------------\n\n")
#   if there is no standard mic:
#   print(sr.Microphone.list_microphone_names())
#   mic = sr.Microphone(device_index=2)"""


class Voice:
    def __init__(self):
        pass

    def listen(self):
        result_google = ""
        result_sphinx = ""
        print("listening...")
        with mic as source:
            audio1 = r.listen(source)

        #   print(type(audio1))
        print("attempting google")
        try:
            text = r.recognize_google(audio1, language="de-DE")
            result_google = f"Online (Google): {text}"
        except sr.UnknownValueError:
            result_google = "Google Speech didn't recognize anything (UnknownValueError)"
        print(result_google)

        print("attempting sphinx")
        try:
            text = r.recognize_sphinx(audio1)
            result_sphinx = f"Offline (Sphinx): {text}"
        except sr.UnknownValueError:
            result_sphinx = "Pocketsphinx didn't recognize anything (UnknownValueError)"
        print(result_sphinx)

        result = f"{result_google}\n\n{result_sphinx}\n------------------------------\n\n"
        return result


vc = Voice()
print(vc.listen())
