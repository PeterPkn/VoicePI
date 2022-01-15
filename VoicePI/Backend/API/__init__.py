
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
from time import sleep

from ThreadManager import ThreadManager

from Music import MusicPlayer
from Voice import listen




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

@app.route('/silentmode', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    # voice pi should handle the input and do whatever it needs to here, then the response should be sent out as text.
    #if contains amogus...


    a_string = record['msg']
    matches = ["amogus", "among us", "sus", "sussy"]

    
    music = MusicPlayer(a_string)
    
    if 'play' in a_string:
        music.start()
        #while infos are not set, waitm, then return it all
        #while(infos[0] == ''):
        #    print(infos)
        #    sleep(0.1)
        infos = music.getMetadata()
        return jsonify({'answ':f'Started playing: {infos[0]} from {infos[1]}'})

    if 'stop' in a_string:
        ThreadManager.StopAllMusic()
        return jsonify({'answ':'Stopping all Music.'})

    if any(x in a_string.lower() for x in matches):
        return jsonify({'answ':'You sussy baka.'})

    if 'listen' in a_string:
        req = listen()
        print(req['query'])
        music = MusicPlayer(req['query'].replace('play','').replace('spiele', ''))
        if 'play' in req or 'spiele' in req['query']:
            music.start()
            #while infos are not set, waitm, then return it all
            #while(infos[0] == ''):
            #    print(infos)
            #    sleep(0.1)
            infos = music.getMetadata()
            return jsonify({'answ':f'Started playing: {infos[0]} from {infos[1]}'})



    return jsonify({'answ':'VoicePI says haha funny lol'})


if __name__ == '__main__':
    app.run(debug=True)