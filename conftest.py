import allure
import pytest
import requests
from constants import const as c
from objects import basic_functions as b


@allure.title("Создать нового курьера")
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
        response = requests.post(f'{c.host}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass

    response_id = requests.post(f"{c.host}/api/v1/courier/login", data={"login": login, "password": password})
    courier_id = response_id.json()["id"]

    with allure.step("Удалить курьера"):
        requests.delete(f"{c.host}/api/v1/courier/:id", data={"id": courier_id})


@pytest.fixture(scope='class')
def courier_auth(new_courier):
    url = f"{c.host}/api/v1/courier/login"

    payload = {
        "login": new_courier[0],
        "password": new_courier[1]
    }

    response = requests.post(url, data=payload)
    courier_id = 0
    if response.status_code == 200:
        courier_id = response.json()["id"]
    return courier_id
