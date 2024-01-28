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
        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.name
        }

        response = requests.post(c.EP_COURIER, data=payload)
        return response

    @allure.step("Авторизоваться под курьером в системе")
    def login_courier(self):
        payload = {
            "login": self.login,
            "password": self.password
        }
        response = requests.post(c.EP_COURIER_LOGIN, data=payload)
        return response

    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(courier_id):
        payload = {
            "id": courier_id
        }

        response = requests.delete(c.EP_COURIER_ID, data=payload)
        return response
