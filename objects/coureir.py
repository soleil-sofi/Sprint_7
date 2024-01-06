import allure
import requests
from constants import const as c


class Courier:

    def __init__(self, login, password, name=None):
        self.login = login
        self.password = password
        self.name = name

    @allure.step("Создать курьера")
    def create_courier(self):
        url = f"{c.host}/api/v1/courier"

        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.name
        }

        response = requests.post(url, data=payload)
        return response

    @allure.step("Авторизоваться под курьером в системе")
    def login_courier(self):
        url = f"{c.host}/api/v1/courier/login"

        payload = {
            "login": self.login,
            "password": self.password
        }
        response = requests.post(url, data=payload)
        return response

    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(courier_id):
        url = f"{c.host}/api/v1/courier/:id"

        payload = {
            "id": courier_id
        }

        response = requests.delete(url, data=payload)
        return response
