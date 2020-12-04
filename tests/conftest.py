""" Configure the testing requirements """
import pytest
from main import app as _app


@pytest.fixture(scope='session')
def app():
    """
    Get the Testing app with config
    :return: Testing app instance
    """
    _app.config['TESTING'] = True
    _app.config['WTF_CSRF_ENABLED'] = False
    _app.config['DEBUG'] = True

    return _app


@pytest.fixture(scope='session')
def client(app):
    """
    Get the Testing Client
    :param app: Instance
    :return: Testing Client
    """
    with app.app_context():
        yield app.test_client()
