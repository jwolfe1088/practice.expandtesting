import requests

def test_login(api_client, email, password):
    response = api_client.user_login(email, password)
    assert response.status_code == 200

def test_login_contains_token(api_client, email, password):
    response = api_client.user_login(email, password)
    assert "token" in response.json()["data"]

def test_invalid_login(api_client, email):
    wrong_password = "WrongPassword"
    response = api_client.user_login(email, wrong_password)
    assert response.status_code == 401