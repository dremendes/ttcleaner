from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """
    answer / GET
    """
    return {
        'userID': 1,
        'title': 'Flask React App',
        'completed': False
    }
