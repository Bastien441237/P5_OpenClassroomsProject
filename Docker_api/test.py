from conftest import client
import json

def test_should_status_code_ok_get(client):
    response = client.get('/')
    assert response.status_code == 200

def test_should_return_msg(client):
    response = client.get('/')
    data = response.data.decode()
    assert data == "API Flask pour utilisation dans Streamlit, voici l'URL : https://categoriser-automatiquement-des-questions.streamlit.app/"

def test_should_status_code_ok_post(client):
    data = {"text": "Python is very cool !"}
    response = client.post('/predict', json=data)
    assert response.status_code == 200

def test_should_return_predict(client):
    data = {"text": "Python is very cool !"}
    response = client.post('/predict', json=data)
    json_data = json.loads(response.data.decode())
    assert json_data['predicted_tags'] != []