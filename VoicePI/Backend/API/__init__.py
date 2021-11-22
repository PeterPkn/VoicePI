from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class VoiceAPI(Resource):
    def get(self, request_id):
        if  (request_id=='1'):
            return {request_id: 'sus'}
        if  (request_id=='2'):
            return {request_id: 'sussy'}
        if  (request_id=='3'):
            return {request_id: 'baka'}
        if  (request_id=='4'):
            return {request_id: 'impostor'}
        
        

api.add_resource(VoiceAPI, '/<string:request_id>')


if __name__ == '__main__':
    app.run(debug=True)