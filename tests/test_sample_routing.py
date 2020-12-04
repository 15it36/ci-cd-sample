""" Test the sample Routing func """


def test_sample_routing(client):
    """
    Test sample routing func
    :param client: Testing Client
    :return: 200 ok
    """
    response = client.get('/')

    assert response.status_code == 200
    assert response.data
