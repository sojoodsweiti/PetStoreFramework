import pytest
import requests
from assertpy import assert_that


@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/v2"


@pytest.fixture
def new_pet():
    return {
        "id":  9223372036854744894,
        "category": {"id": 0, "name": "string"},
        "name": "Test Pet",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }


@pytest.fixture
def pet_id(base_url, new_pet):
    response = requests.post(f"{base_url}/pet", json=new_pet)
    assert response.status_code == 200
    pet_id = response.json()["id"]
    return pet_id


def test_get_pet(base_url, pet_id):
    response = requests.get(f"{base_url}/pet/{pet_id}")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()["name"]).is_equal_to("Test Pet")
    assert_that(response.json()["status"]).is_equal_to("available")


def test_create_pet(base_url, new_pet):
    response = requests.post(f"{base_url}/pet", json=new_pet)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to(new_pet)


def test_update_pet(base_url, pet_id):
    updated_pet = {"id": pet_id, "category": {"id": 0, "name": "string"},
                   "name": "Updated Pet",
                   "photoUrls": ["string"],
                   "tags": [{"id": 0, "name": "string"}],
                   "status": "sold"}
    response = requests.put(f"{base_url}/pet", json=updated_pet)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to(updated_pet)
    assert_that(response.json()["name"]).is_equal_to("Updated Pet")
    assert_that(response.json()["status"]).is_equal_to("sold")





