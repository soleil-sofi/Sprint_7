import allure
import requests
from constants import const as c


class Order:

    def __init__(self, color: list = [], first_name: str = "Testname", last_name: str = "Testname", address: str = "smth",
                 metro_station: int = 1, phone: str = "+7 800 355 35 35", rent_time: int = 4,
                 delivery_date: str = "2024-01-07", comment: str = "test"):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.metro_station = metro_station
        self.phone = phone
        self.rent_time = rent_time
        self.delivery_date = delivery_date
        self.comment = comment
        self.color = color

    @allure.step("Создать заказ")
    def create_order(self):
        payload = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "address": self.address,
            "metroStation": self.metro_station,
            "phone": self.phone,
            "rentTime": self.rent_time,
            "deliveryDate": self.delivery_date,
            "comment": self.comment,
            "color": self.color
        }

        response = requests.post(c.EP_ORDERS, data=payload)
        return response

    @allure.step("Получить список заказов")
    def get_orders_list(self, courier_id=None):
        params = {
            "courierId": courier_id,
            "nearestStation": [str(self.metro_station)],
            "limit": 1,
            "page": None
        }

        response = requests.get(c.EP_ORDERS, params=params)
        return response

    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(order_id):
        payload = {
            "track": order_id
        }

        response = requests.put(c.EP_ORDERS_CANCEL, data=payload)
        return response
