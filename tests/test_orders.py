import allure
import pytest
from objects.orders import Order


@allure.suite("Тесты метода создания заказа")
class TestOrders:

    @allure.title("Создание заказа с разными цветами самоката")
    @pytest.mark.parametrize("color", [[], ['BLACK'], ['GREY'], ['BLACK', 'GREY']])
    def test_order_with_different_colors(self, color):
        order = Order(color=color)
        response = order.create_order()
        assert response.status_code == 201
        assert "track" in response.json()

        track = response.json()["track"]
        order.cancel_order(track)

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        order = Order()
        response = order.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json() and response.json()["orders"] != []
