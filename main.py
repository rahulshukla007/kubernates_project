from flask import Flask, request
import logging
from flask_restful import Resource, Api
import sys

app = Flask(__name__)
api = Api(app)

logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG)
logger=logging.getLogger(__name__)



    
class HelloWorld(Resource):
    def get(self):
        x = 5
        logging.debug(f'This is debug varible {x}')
        return {'hello': 'world'}

class Dashboard(Resource):
    import pdb, pdb;
    def get(self):
        dict = {'a': 100, 'b': 200, 'c': 300}
        list = []
        for i in dict:
            list.append(dict[i])
        final = sum(list)
        print("Sum of list:", final)
        return {'board': 'this is newley on boarded dashboard'}

    

    def post(self):
        try:
            data = request.json
            print(data['rating'][1])
        except Exception as e:
            print(e)
            return 'Server shutting down...'
        
        return data

class TakeInput(Resource):
    def get(self, integer):
        integer = int(integer)
        num = 0
        for i in range(0,integer+1):
            num = num + i
        print("final number is", num)
        return {"final number is" : num}

    


api.add_resource(HelloWorld, '/')
api.add_resource(Dashboard, '/dash')
api.add_resource(TakeInput, '/input/<string:integer>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)