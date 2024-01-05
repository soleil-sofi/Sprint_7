import pytest
import requests
import random
import string
from constants import const as c


@pytest.fixture(scope='class')
def new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{c.host}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


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
