from flask import Flask
from flask_cors import CORS, cross_origin
from Utils.utils import classify_email

# Initialize the flask app
app = Flask(__name__)
# Enable CORS to allow cross origin requests
cors = CORS(app)


# A simple route to test app working
@app.route('/')
def test():
    return 'App works!'


# The main route that enables passing of data to the model for classification
@app.route('/classify', methods=["POST"])
@cross_origin()
def classify():
    """
    The classify route accepts the email in a bytes format which is then converted
    to a string and finally a dictionary object. This is the passed to the prediction function.
    :return: A response object containing a dictionary of the cleaned email string and the prediction result.
    """
    return classify_email()


if __name__ == '__main__':
    app.run()
