""" Test Payment Routes """


def test_payment_routes(client):
    """
    Test Payment Routes
    :param client: testing client
    :return: 200 ok
    """
    response = client.post('api/v1/payment/')

    assert response.status_code == 200
