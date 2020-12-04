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


def test_sample_post(client):
    """
    Test Sample POST func
    :param client: Test Client
    :return: 200 ok
    """
    response = client.post('/')

    assert response.status_code == 200
    assert response.data
