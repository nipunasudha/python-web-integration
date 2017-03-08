import requests
from flask import Flask, request

app = Flask(__name__)

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
    return "Hello World!"


if __name__ == "__main__":
    app.run()