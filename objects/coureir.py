import requests
import json
from constants import const as c


class Courier:

    def __init__(self, login, password, name):
        self.login = login
        self.password = password
        self.name = name

    def create_courier(self):
        url = f"{c.host}/api/v1/courier"

        payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.name
        }

        response = requests.post(url, data=payload)
        return response

    def courier_login(self):
        url = f"{c.host}/api/v1/courier/login"

        payload = {
            "login": self.login,
            "password": self.password
        }

        response = requests.post(url, data=payload)
        return response

    def delete_corier(self, courier_id):
        url = f"{c.host}/api/v1/courier/:id"

        payload = {
            "id": courier_id
        }

        response = requests.delete(url, data=payload)
        return response
