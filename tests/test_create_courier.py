import allure
import pytest
from objects import basic_functions as b
from objects.coureir import Courier


@allure.suite("Тесты метода создания курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_successfully(self):
        login = b.generate_random_string(6)
        password = b.generate_random_string(8)
        name = b.generate_random_string(4)
        courier = Courier(login, password, name)
        response = courier.create_courier()
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        courier_id = courier.login_courier().json()["id"]
        courier.delete_courier(courier_id)

    @allure.title("Создание курьера без обязательных полей")
    @pytest.mark.parametrize("login, password", [(b.generate_random_string(6), None),
                                                 (None, b.generate_random_string(6))])
    def test_create_courier_empty_fields(self, login, password):
        courier = Courier(login, password)
        response = courier.create_courier()
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Создание неуникального курьера")
    def test_create_courier_with_existing_login(self, new_courier):
        login, password, name = new_courier
        courier = Courier(login, password)
        response = courier.create_courier()
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]
