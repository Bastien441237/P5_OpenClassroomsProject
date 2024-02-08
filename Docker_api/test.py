import pytest
import json
from Moreno_Bastien_5_code_API_022024 import app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app"""
    with app.test_client() as client:
        yield client

def test_msg(client):
    """Test the / endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'API Flask pour utilisation dans Streamlit, voici l\'URL : https://categoriser-automatiquement-des-questions.streamlit.app/'

def test_predict(client):
    """Test the /predict endpoint"""
    data = {'text': 'Sample text for prediction'}
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert 'predicted_tags' in json.loads(response.data)

def test_invalid_json(client):
    """Test for invalid JSON data"""
    response = client.post('/predict', data='not a JSON')
    assert response.status_code == 400

def test_missing_text_field(client):
    """Test for missing 'text' field in JSON data"""
    data = {'other_field': 'some_value'}
    response = client.post('/predict', json=data)
    assert response.status_code == 400
    assert 'error' in json.loads(response.data)

if __name__ == "__main__":
    pytest.main()
