from app import app
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = app

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

def test_http_html_get(test_client):
    """
    GIVEN a Flask application
    WHEN the "/HTTP" page is requested with a get (GET)
    AND we do not pass a Accept header
    THEN check that the response is 200 and we get back <p>Hello, World<p>
    """
    response = test_client.get("/HTTP")
    assert response.status_code == 200
    assert  b'<p>Hello, World</p>' == response.data

def test_http_html_post(test_client):
    """
    GIVEN a Flask application
    WHEN the "/HTTP" page is requested with a post (OIST)
    AND we do not pass a Accept header
    THEN check that the response is 200 and we get back <p>Hello, World<p>
    """
    response = test_client.post("/HTTP")
    assert response.status_code == 200
    assert  b'<p>Hello, World</p>' == response.data

def test_http_json_get(test_client):
    """
    GIVEN a Flask application
    WHEN the "/HTTP" page is requested with a get (GET)
    AND we do pass an Accept header with "application/json"
    THEN check that the response is 200 and we get back json {'message': 'Good morning'}
    """
    response = test_client.get("/HTTP", headers={"Accept": "application/json"})
    assert response.status_code == 200
    json_data = response.json
    assert json_data['message'] == "Good morning"

def test_http_json_post(test_client):
    """
    GIVEN a Flask application
    WHEN the "/HTTP" page is requested with a post (OIST)
    AND we do pass an Accept header with "application/json"
    THEN check that the response is 200 and we get back json {'message': 'Good morning'}
    """
    response = test_client.post("/HTTP", headers={"Accept": "application/json"})
    assert response.status_code == 200
    json_data = response.json
    assert json_data['message'] == "Good morning"