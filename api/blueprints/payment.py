""" Payment Blueprint """
import razorpay
import json
from flask import Blueprint, request, render_template

payment_bp = Blueprint('payment_blueprint', __name__)

razorpay_client = razorpay.Client(auth=("Flask", "1.1.2"))


@payment_bp.route('/payment-home')
def payment_page():
    """
    Initial Payment page
    :return: Template
    """
    return render_template('payment.html')


@payment_bp.route('/capture', methods=['POST'])
def payment():
    """
    Request Payment Page
    :return: payment page
    """
    payment_id = request.form['razorpay_payment_id']
    print(payment_id)
    result = razorpay_client.payment.fetch('pay_GAS4AXTBRNKVzD')
    print(result)
    return json.dumps(razorpay_client.payment.fetch(payment_id))
