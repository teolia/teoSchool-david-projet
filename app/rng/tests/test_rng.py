from flask import Flask, Response
import sys
import pytest

sys.path.insert(1,'')
import rng

def app():
    app = rng.app
    app.config['TESTING'] = True
    return app

def test_index():
    """
    GIVEN a Flask application 
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = app()

     # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"RNG running on" in response.data

def test_json():
    """
    GIVEN a Flask application 
    WHEN the '/<int>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = app()

     # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/45')
        assert response.status_code == 200
        assert response.content_type == "application/octet-stream"