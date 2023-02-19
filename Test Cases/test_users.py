import pytest
import requests
from assertpy import assert_that
from Base import base_url

# @pytest.fixture
# def base_url():
#     return "https://petstore.swagger.io/v2"


@pytest.fixture
def user_payload():
    return {
        "id": 9223372036854744676,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 0
    }


@pytest.fixture
def credentials():
    return {"username": "testuser",
            "password": "testpassword"
            }


def test_create_user(user_payload):
    response = requests.post(f"{base_url}/user", json=user_payload)
    assert_that(response.status_code).is_equal_to(200)


def test_get_user_by_username(user_payload):
    username = user_payload["username"]
    response = requests.get(f"{base_url}/user/{username}")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to(user_payload)


def test_update_user(user_payload):
    username = user_payload["username"]
    new_name = "Updated User"
    user_payload["username"] = new_name
    response = requests.put(f"{base_url}/user/{username}", json=user_payload)
    assert_that(response.status_code).is_equal_to(200)


def test_delete_user(user_payload):
    username = user_payload["username"]
    response = requests.delete(f"{base_url}/user/{username}")
    assert_that(response.status_code).is_equal_to(200)
    response = requests.get(f"{base_url}/user/{username}")
    assert_that(response.status_code).is_equal_to(404)


def test_login(credentials):
    response = requests.get(f"{base_url}/user/login", json=credentials)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()["message"]).is_equal_to("logged in user session: 1676360253628")


