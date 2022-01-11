from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class VoiceAPI(Resource):
    def get(self, request_id):
        if  (request_id=='voice'):
            return {request_id: 'sus'}
        if  (request_id=='wetter'):
            return {'wetter': 'Wetter ist schön', 'tage': 'montag...'}
        if  (request_id=='3'):
            return {request_id: 'baka'}
        if  (request_id=='4'):
            return {request_id: 'impostor'}
        
        

api.add_resource(VoiceAPI, '/<string:request_id>')


if __name__ == '__main__':
    app.run(debug=True)