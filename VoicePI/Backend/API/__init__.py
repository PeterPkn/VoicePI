from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

import threading

from Music import find_url, play_video




app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO: Wetter API, Silent Mode anfragen & Antworten

def start_music(search):
    play_video(find_url(search[5:]))


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

    infos = ['',''] # pass this to the thread and then read the passed Metadata from here

    a_string = record['msg']
    matches = ["amogus", "among us", "sus", "sussy"]

    th = threading.Thread(target=start_music, args=(a_string,))

    
    if 'play' in a_string:
        th.start()
        #while infos are not set, waitm, then return it all
        return jsonify({'answ':f'Started playing: {a_string[5:]}'})

    if any(x in a_string.lower() for x in matches):
        return jsonify({'answ':'You sussy baka.'})


    return jsonify({'answ':'VoicePI says haha funny lol'})


if __name__ == '__main__':
    app.run(debug=True)