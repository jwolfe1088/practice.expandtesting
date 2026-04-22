import requests

def test_health(api_base_url):
    response = requests.get(f"{api_base_url}/health-check")
    assert response.status_code == 200