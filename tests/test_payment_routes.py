""" Test Payment Routes """


def test_payment_home(client):
    """
    Test Payment Home page
    :param client: Test Client
    :return: 200 ok
    """
    response = client.get('/payment-home')

    assert response.status_code == 200


def test_payment_routes(client):
    """
    Test Payment Routes
    :param client: testing client
    :return: 200 ok
    """
    response = client.post('/capture',
                           data=dict(razorpay_payment_id='pay_GAS4AXTBRNKVzD'))

    assert response.status_code == 200
