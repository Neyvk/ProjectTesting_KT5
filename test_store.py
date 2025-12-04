%%file test_store.py
import pytest
import requests
import time
import allure
from models import Order

url = "https://petstore.swagger.io/v2/store/order"

@pytest.fixture
def test_order():
    return Order(
        id=20,
        petId=101,
        quantity=1,
        shipDate="2025-02-02T10:00:00.000Z",
        status="placed",
        complete=True
    )

@allure.feature("Store API")
@allure.story("Create Order")
def test_post(test_order):
    time.sleep(1)
    response = requests.post(url, json=test_order.model_dump(mode="json"))
    assert response.status_code == 200

@allure.feature("Store API")
@allure.story("Get Order")
def test_get(test_order):
    time.sleep(1)
    order_id = test_order.id
    response = requests.get(f"{url}/{order_id}")
    assert response.status_code == 200

    order_data = Order(**response.json())
    assert order_data.id == test_order.id
    assert order_data.petId == test_order.petId

@allure.feature("Store API")
@allure.story("Delete Order")
def test_delete(test_order):
    time.sleep(1)
    order_id = test_order.id
    response = requests.delete(f"{url}/{order_id}")
    assert response.status_code == 200

    get_response = requests.get(f"{url}/{order_id}")
    assert get_response.status_code == 404

@allure.feature("Store API")
@allure.story("Inventory")
def test_inventory():
    time.sleep(1)
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
    assert response.status_code == 200

    assert response.json()["available"] > 0
