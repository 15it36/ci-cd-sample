""" Factory """
from flask import Flask

from api.blueprints.sample import sample_blueprint

app = Flask(__name__)
app.register_blueprint(sample_blueprint)
