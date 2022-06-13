from flask import Flask
import socket
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi from hostname '+ socket.gethostname() + ' Time here is ' + time.strftime("%H:%M:%S", time.localtime())

