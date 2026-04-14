import pytest
from utils.api_client import APIClient

@pytest.fixture()
def api_client():
    return APIClient()

@pytest.fixture()
def auth_token(api_client, email, password):
    token = api_client.login(email, password)
    return token["token"]