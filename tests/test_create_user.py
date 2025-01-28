import requests
from data import USER_ALREADY_EXISTS_MSG, EMAIL_PASSWORD_NAME_REQUIRED_MSG, SUCCESS_MSG

def test_create_unique_user(base_url, create_user):
    user_payload = create_user
    response = requests.post(f"{base_url}/auth/login", json={
        "email": user_payload["email"],
        "password": user_payload["password"]
    })
    assert response.status_code == 200
    assert response.json()[SUCCESS_MSG] is True

def test_create_existing_user(base_url):
    response = requests.post(f"{base_url}/auth/register", json={
        "email": "existing_user@example.com",
        "password": "password123",
        "name": "ExistingUser"
    })
    assert response.status_code == 403
    assert response.json()["message"] == USER_ALREADY_EXISTS_MSG

def test_create_user_missing_field(base_url):
    response = requests.post(f"{base_url}/auth/register", json={
        "email": "new_user@example.com",
        "password": "password123"
    })
    assert response.status_code == 403
    assert response.json()["message"] == EMAIL_PASSWORD_NAME_REQUIRED_MSG
