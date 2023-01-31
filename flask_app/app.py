from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)

def run_request():
    index = int(request.json['index'])
    list = ['Hello!', 'Hola!', 'Hey!']
    return list[index]

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World! from nginx and Flask application. Try to send a POST request'
    else:
        return run_request()

