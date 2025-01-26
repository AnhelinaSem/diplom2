import requests
from data import BASE_URL
from utils import create_unique_email

def test_create_unique_user(base_url, user_payload):
    unique_email = create_unique_email()
    user_payload["email"] = unique_email
    response = requests.post(f"{base_url}/auth/register", json=user_payload)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_create_existing_user(base_url):
    response = requests.post(f"{base_url}/auth/register", json={
        "email": "existing_user@example.com",
        "password": "password123",
        "name": "ExistingUser"
    })
    assert response.status_code == 403
    assert response.json()["message"] == "User already exists"

def test_create_user_missing_field(base_url):
    response = requests.post(f"{base_url}/auth/register", json={
        "email": "new_user@example.com",
        "password": "password123"
    })
    assert response.status_code == 403
    assert response.json()["message"] == "Email, password and name are required fields"
