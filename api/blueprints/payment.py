""" Payment Blueprint """
from flask import Blueprint

payment_bp = Blueprint('payment_blueprint', __name__)


@payment_bp.route('/')
def payment():
    """
    Request Payment Page
    :return: payment page
    """
    pass
