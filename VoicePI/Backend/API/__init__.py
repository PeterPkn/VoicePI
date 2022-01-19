from os import error
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
from time import sleep

from ThreadManager import ThreadManager

from Keyword import Keyword

Keyword.createKeywords()

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



@app.route('/silentmode', methods=['POST'])
def update_record():
    print(request.data)
    record = json.loads(request.data)

    a_string = record['msg'].lower()

    return Keyword.findKeyword(a_string)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")