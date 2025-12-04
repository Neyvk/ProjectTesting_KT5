%%file test_pet.py
import pytest
import requests
import time
import allure
from models import Pet, Category

url = "https://petstore.swagger.io/v2/pet"

@pytest.fixture
def test_pet():
    return Pet(
        id=101,
        category=Category(id=1, name="dogs"),
        name="Rex",
        photoUrls=["https://example.com/rex.jpg"],
        tags=[{"id": 1, "name": "friendly"}],
        status="available"
    )

@allure.feature("Pet API")
@allure.story("Create Pet")
def test_post(test_pet):
    time.sleep(1)
    response = requests.post(url, json=test_pet.dict())
    assert response.status_code == 200

@allure.feature("Pet API")
@allure.story("Get Pet")
def test_get(test_pet):
    time.sleep(1)
    response = requests.get(f"{url}/{test_pet.id}")
    assert response.status_code == 200

    pet_data = Pet(**response.json())
    assert pet_data.name == test_pet.name
    assert pet_data.status == test_pet.status

@allure.feature("Pet API")
@allure.story("Update Pet")
def test_put(test_pet):
    time.sleep(1)
    updated_pet = test_pet.copy(update={"name": "Max"})
    response = requests.put(url, json=updated_pet.dict())
    assert response.status_code == 200

    time.sleep(1)
    get_response = requests.get(f"{url}/{test_pet.id}")
    pet_data = Pet(**get_response.json())
    assert pet_data.name == "Max"

@allure.feature("Pet API")
@allure.story("Delete Pet")
def test_delete(test_pet):
    time.sleep(1)
    response = requests.delete(f"{url}/{test_pet.id}")
    assert response.status_code == 200

    get_response = requests.get(f"{url}/{test_pet.id}")
    assert get_response.status_code == 404
