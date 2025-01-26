import requests
from data import BASE_URL

def test_login_existing_user(base_url):
    response = requests.post(f"{base_url}/auth/login", json={
        "email": "existing_user@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_login_invalid_credentials(base_url):
    response = requests.post(f"{base_url}/auth/login", json={
        "email": "invalid_user@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["message"] == "email or password are incorrect"
