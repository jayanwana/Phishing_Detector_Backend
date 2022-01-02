import json

from flask import Flask
from flask import jsonify, make_response, request, Response
from flask_cors import CORS, cross_origin
from Utils.utils import make_prediction

app = Flask(__name__)
cors = CORS(app)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/classify', methods=["POST"])
@cross_origin()
def classify_email():
    email = json.loads(str(request.data, 'utf-8'))['text']
    if email:
        result = make_prediction(email)
        print(result['result'])
    else:
        result = {}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
