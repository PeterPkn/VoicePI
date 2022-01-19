from os import error
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
from time import sleep

from ThreadManager import ThreadManager

from Music import MusicPlayer
from Video import VideoPlayer
from Voice import listen, speak, listen_in_bg
from Keyword import Keyword


def func():
    pass

stop_listening = func

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO: Wetter API, Silent Mode anfragen & Antworten

def start_music(search, infos):
    play_video(find_url(search[5:]), infos)


@app.route('/wetter', methods=['GET'])
def wetter():
    return {'wetter': 'wetter'}

@app.route('/specific', methods=['GET'])
def specific():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    return {'id_is':id}



def play_action(a_string):
    music = MusicPlayer(a_string)
    music.start()
    infos = music.getMetadata()
    speak(f'Started playing: {infos[0]} from {infos[1]}')
    return jsonify({'answ':f'Started playing: {infos[0]} from {infos[1]}'})

def listenbg_action(a_string):
    if 'listen bg stop' in a_string:
        try:
            stop_listening()
            return jsonify({'answ':f'Stopped Listening in the Background'})
        except error:
            print('Could not stop Background Listening!')
            
    stop_listening = listen_in_bg()
    return jsonify({'answ':f'Listening in the Background'})

def stop_action(a_string):
    ThreadManager.StopAllMusic()
    speak('Stopping all Music.')
    return jsonify({'answ':'Stopping all Music.'})

def speak_action(a_string):
    speak(a_string[5:])
    return {'answ':a_string[5:]}

def listen_action(a_string):
    req = listen()
    print(req['query'])
        
    if 'play' in req or 'spiele' in req['query']:
        music = MusicPlayer(req['query'].replace('play','').replace('spiele', ''))
        infos = music.getMetadata()
        speak(f'Started playing: {infos[0]} from {infos[1]}')
        music.start()
            
        return jsonify({'answ':f'Started playing: {infos[0]} from {infos[1]}'})

    elif 'show' in req or 'zeige' in req['query']:
        video = VideoPlayer(req['query'].replace('play','').replace('spiele', ''))
        infos = video.getMetadata()
        speak(f'Started playing: {infos[0]} from {infos[1]}')
        video.start()

def show_action(a_string):
    video = VideoPlayer(a_string.replace('play','').replace('spiele', ''))
    infos = video.getMetadata()
    speak(f'Started playing: {infos[0]} from {infos[1]}')
    video.start()

def sussy_action(a_string):
    speak('You sussy baka!')
    return jsonify({'answ':'You sussy baka.'})

Keyword('play',play_action,1 )
Keyword('spiele',play_action,1 )
Keyword('listen bg',listenbg_action,2 )
Keyword('stop',stop_action,3 )
Keyword('speak',speak_action,4 )
Keyword('listen',listen_action,5 )
Keyword('show',show_action,6 )
Keyword('zeige',show_action,6 )


Keyword('sus',sussy_action,100 )
Keyword('among us',sussy_action,100 )
Keyword('amogus',sussy_action,100 )
Keyword('sussy',sussy_action,100 )

@app.route('/silentmode', methods=['POST'])
def update_record():
    print(request.data)
    record = json.loads(request.data)

    a_string = record['msg'].lower()

    Keyword.findKeyword(a_string)

    return jsonify({'answ':'VoicePI says haha funny lol'})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")