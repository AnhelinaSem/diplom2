import requests
from data import BASE_URL
from data import INCORRECT_ID_MSG, INGREDIENT_IDS_REQUIRED

def test_get_ingredients(base_url):
    response = requests.get(f"{base_url}/ingredients", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    json_response = response.json()
    assert json_response["success"] is True
    assert "data" in json_response


def test_create_order_with_auth(base_url, headers, valid_ingredients):
    response = requests.post(f"{base_url}/orders",
                             headers=headers,
                             json={"ingredients": valid_ingredients})

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["success"] is True

def test_create_order_without_auth(base_url):
    response = requests.post(f"{base_url}/orders", headers={"Accept": "application/json"}, json={
        "ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
    })
    assert response.status_code == 400
    assert "application/json" in response.headers["Content-Type"]
    json_response = response.json()
    assert json_response["message"] == INCORRECT_ID_MSG

def test_create_order_without_ingredients(base_url, headers):
    response = requests.post(f"{base_url}/orders", headers=headers, json={})
    assert response.status_code == 400
    assert "application/json" in response.headers["Content-Type"]
    json_response = response.json()
    assert json_response["message"] == INGREDIENT_IDS_REQUIRED

def test_create_order_invalid_ingredient_hash(base_url, headers):
    response = requests.post(f"{base_url}/orders", headers=headers, json={
        "ingredients": ["invalid_hash"]
    })
    assert response.status_code == 400
    assert "application/json" in response.headers["Content-Type"]
    json_response = response.json()
    assert json_response["message"] == INCORRECT_ID_MSG
