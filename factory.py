""" Factory """
from flask import Flask

from api.blueprints.payment import payment_bp
from api.blueprints.sample import sample_blueprint

app = Flask(__name__)
app.register_blueprint(sample_blueprint)
app.register_blueprint(payment_bp)
