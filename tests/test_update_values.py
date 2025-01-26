import requests
from data import BASE_URL

def test_update_user_with_auth(base_url, headers):
    response = requests.patch(f"{base_url}/auth/user", headers=headers, json={
        "name": "UpdatedName"
    })
    assert response.status_code == 200
    assert response.json()["user"]["name"] == "UpdatedName"

def test_update_user_without_auth(base_url):
    response = requests.patch(f"{base_url}/auth/user", json={
        "name": "UpdatedName"
    })
    assert response.status_code == 401
    assert response.json()["message"] == "You should be authorised"
