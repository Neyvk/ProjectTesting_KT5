%%file test_user.py
import pytest
import requests
import time
import allure
from models import User

url = "https://petstore.swagger.io/v2/user"

@pytest.fixture
def test_user():
    return User(
        id=88,
        username="shpatovich",
        firstName="Andrew",
        lastName="S",
        email="shpatovichad@ithub.ru",
        password="12345",
        phone="",
        userStatus=1
    )

@allure.feature("User API")
@allure.story("Create user")
def test_post(test_user):
    time.sleep(1)
    response = requests.post(url, json=test_user.dict())
    assert response.status_code == 200

@allure.feature("User API")
@allure.story("Get user")
def test_get(test_user):
    time.sleep(1)
    username = test_user.username
    response = requests.get(f"{url}/{username}")
    assert response.status_code == 200

    user_data = User(**response.json())
    assert user_data.username == test_user.username
    assert user_data.email == test_user.email

@allure.feature("User API")
@allure.story("Update user")
def test_put(test_user):
    time.sleep(1)
    username = test_user.username
    updated_user = test_user.copy(update={"firstName": "Maomao"})
    response = requests.put(f"{url}/{username}", json=updated_user.dict())
    assert response.status_code == 200

    time.sleep(1)
    get_response = requests.get(f"{url}/{username}")
    user_data = User(**get_response.json())
    assert user_data.firstName == "Maomao"

@allure.feature("User API")
@allure.story("Delete user")
def test_delete(test_user):
    time.sleep(1)
    username = test_user.username
    response = requests.delete(f"{url}/{username}")
    assert response.status_code == 200

    get_response = requests.get(f"{url}/{username}")
    assert get_response.status_code == 404
