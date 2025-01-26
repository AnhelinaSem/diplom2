import pytest
import requests
from data import BASE_URL
from utils import generate_random_string, create_unique_email

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def existing_user():
    return {
        "email": "existing_user@example.com",
        "password": "password123"
    }

@pytest.fixture(scope="function")
def auth_token(base_url, existing_user):
    # Get fresh auth token
    response = requests.post(f"{base_url}/auth/login", json={
        "email": existing_user["email"],
        "password": existing_user["password"]
    })
    assert response.status_code == 200
    return response.json()["accessToken"]

@pytest.fixture(scope="function")
def headers(auth_token):
    return {
        "Authorization": auth_token
    }

@pytest.fixture(scope="function")
def valid_ingredients(base_url):
    response = requests.get(f"{base_url}/ingredients")
    assert response.status_code == 200
    ingredients_data = response.json()
    return [item["_id"] for item in ingredients_data["data"][:2]]


@pytest.fixture(scope="function")
def user_payload():
    email = create_unique_email()
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
        "email": email,
        "password": password,
        "name": first_name
    }