import pytest
import requests
from assertpy import assert_that
from Base import base_url

# @pytest.fixture
# def base_url():
#     return "https://petstore.swagger.io/v2"


@pytest.fixture
def order_data():
    return {
          "id": 0,
          "petId": 0,
          "quantity": 0,
          "shipDate": "2023-02-12T12:01:33.857Z",
          "status": "placed",
          "complete": True
    }

@pytest.fixture
def order_id(order_data):
    response = requests.post(f"{base_url}/store/order", json=order_data)
    order_id = response.json()["id"]
    return order_id


def test_place_an_order_for_a_pet(order_data):
    response = requests.post(f"{base_url}/store/order", json=order_data)
    assert_that(response.status_code).is_equal_to(200)
    order = response.json()
    assert_that(order).contains_key("id", "petId")
    assert_that(order["status"]).is_equal_to("placed")


def test_get_order_by_id(order_data, order_id):
    response = requests.get(f"{base_url}/store/order/{order_id}")
    order = response.json()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(order["id"]).is_equal_to(order_id)
    assert_that(order["complete"]).is_instance_of(bool)


def test_delete_order_by_id(order_data, order_id):
    response = requests.delete(f"{base_url}/store/order/{order_id}")
    assert_that(response.status_code).is_equal_to(200)
    response = requests.get(f"{base_url}/store/order/{order_id}")
    assert_that(response.status_code).is_equal_to(404)


def test_get_inventory_by_status():
    response = requests.get(f"{base_url}/store/inventory")
    assert response.status_code == 200
    inventory = response.json()
    assert_that(inventory).contains_key("sold")


