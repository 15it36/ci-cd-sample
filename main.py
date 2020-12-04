""" CI/CD Flask sample project """
from flask import Flask

app = Flask(__name__)


@app.route('/')
def response():
    """
    Sample Routing func
    :return: String
    """
    return 'Welcome to ci/cd sample project'


@app.route('/', methods=['POST'])
def request():
    """
    POST sample method
    :return: string
    """
    return 'Sample POST method'
