import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
# Tornado serving utility
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.ioloop import IOLoop
# Import utilities
import utilities
# Import image processor
import image_processor as im
import os

cwd = os.getcwd()
cam = im.init_camera(0)
requestCount = 0
app = Flask(__name__)
CORS(app)
# SENDING A POST REQUEST
r = requests.post("http://httpbin.org/post", data={'foo': 'bar'})
print(r.text)


# RECIEVING POST REQUEST
@app.route('/post', methods=['POST'])
def result():
    print(request.form['foo'])  # should display 'bar'
    return 'Received !'  # response to your request.


# SIMPLE ROUTE
@app.route("/")
def hello():
    global requestCount, cam
    im.read_camera(cam)
    requestCount += 1
    return jsonify(["Hello World! Backend recieved " + str(requestCount) + " requests."])
    # return send_file("D:\\lumino\\web\\photoFromCam.jpg", mimetype='image/gif')


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
