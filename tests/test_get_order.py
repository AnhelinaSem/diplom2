import requests
from data import BASE_URL

def test_get_orders_with_auth(base_url, headers):
    response = requests.get(f"{base_url}/orders", headers=headers)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    json_response = response.json()
    assert json_response["success"] is True

def test_get_orders_without_auth(base_url):
    response = requests.get(f"{base_url}/orders")
    assert response.status_code == 401
    assert "application/json" in response.headers["Content-Type"]
    json_response = response.json()
    assert json_response["message"] == "You should be authorised"
