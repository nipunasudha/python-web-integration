import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
# Tornado serving utility
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
# Import image processor
import image_processor as im
import os
import pprint
import json
import server_tools as st

cwd = os.getcwd()
cam = im.init_camera(0)
requestCount = 0
app = Flask(__name__)
CORS(app)
print("Initiated.")


# RECIEVING GET REQUEST
@app.route('/get', methods=['GET'])
def result():
    # print(request.form['foo'])  # should display 'bar'
    pprint.pprint(request.args)  # should display 'bar'
    return 'Received !'  # response to your request.


# RECIEVING POST REQUEST
@app.route('/post', methods=['POST'])
def resultp():
    st.parse_command(request)
    return json.dumps(["Recieved!"])


# SIMPLE ROUTE
@app.route("/")
def hello():
    # somestuff
    print("SIMPLE ROUTE")


def stop_tornado():
    IOLoop.instance().stop()


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
