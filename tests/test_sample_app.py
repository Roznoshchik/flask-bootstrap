import pytest


@pytest.fixture
def app():
    import sys
    sys.path.append('.')

    from sample_app import create_app

    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    resp = client.get('/')
    assert resp.status == 200
