from flask import Flask
from flask import request
from main import main as process 
try:
    from config import bot_token
except ImportError as e:
    print('Config file is missing, use config.example.py')
    raise e

app = Flask(__name__)

@app.route('/' + bot_token, methods=['GET', 'POST'])
def receive_hook():
    if request.json is not None:
        return process(request.json)
    return ''