import requests
from constants import const as c


class Order:

    def __init__(self, color: list, first_name: str = "Testname", last_name: str = "Testname", address: str = "smth",
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

    def create_order(self):
        url = f"{c.host}/api/v1/orders"

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

        response = requests.post(url, data=payload)
        return response

    def get_orders_list(self, courier_id):
        url = f"{c.host}/api/v1/orders"

        params = {
            "courierId": courier_id,
            "nearestStation": [str(self.metro_station)],
            "limit": 1,
            "page": None
        }

        response = requests.get(url, params=params)
        return response

    @staticmethod
    def cancel_order(order_id):
        url = f"{c.host}/api/v1/orders/cancel"

        payload = {
            "track": order_id
        }

        response = requests.put(url, data=payload)
        return response
