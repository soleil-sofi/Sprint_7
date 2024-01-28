import allure
import pytest
import requests
from constants import const as c
from objects import basic_functions as b


@allure.title("Создание нового курьера")
@pytest.fixture(scope='class')
def new_courier():
    login_pass = []
    login = b.generate_random_string(10)
    password = b.generate_random_string(10)
    first_name = b.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    with allure.step("Создать курьера"):
        response = requests.post(f'{c.HOST}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass

    response_id = requests.post(f"{c.HOST}/api/v1/courier/login", data={"login": login, "password": password})
    courier_id = response_id.json()["id"]

    with allure.step("Удалить курьера"):
        requests.delete(f"{c.HOST}/api/v1/courier/:id", data={"id": courier_id})


@allure.title("Получение логина созданного курьера")
@pytest.fixture(scope='class')
def correct_login(new_courier):
    return new_courier[0]


@allure.title("Получение пароля созданного курьера")
@pytest.fixture(scope='class')
def correct_password(new_courier):
    return new_courier[1]
