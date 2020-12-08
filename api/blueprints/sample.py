""" CI/CD Flask sample project """
from flask import Blueprint

sample_blueprint = Blueprint('sample_blueprint', __name__)


@sample_blueprint.route('/')
def response():
    """
    Sample Routing func
    :return: String
    """
    return 'Welcome to ci/cd sample project'


@sample_blueprint.route('/', methods=['POST'])
def request():
    """
    POST sample method
    :return: string
    """
    return 'Sample POST method'
