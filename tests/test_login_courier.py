import allure
import pytest
from pytest_lazyfixture import lazy_fixture
from objects.coureir import Courier
from objects import basic_functions as b


@allure.suite("Тесты метода авторизации курьера")
class TestLoginCourier:

    @allure.title("Авторизация курьера с корректными входными данными")
    def test_login_courier_successfully(self, correct_login, correct_password):
        courier = Courier(correct_login, correct_password)
        response = courier.login_courier()
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация курьера с пустыми полями")
    @pytest.mark.parametrize("login, password", [(lazy_fixture('correct_login'), None),
                                                 (None, lazy_fixture('correct_password'))])
    def test_login_courier_with_empty_fields(self, login, password):
        courier = Courier(login, password)
        response = courier.login_courier()
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json()["message"]

    @allure.title("Авторизация курьера с некорректными входными данными")
    @pytest.mark.parametrize("login, password", [(lazy_fixture('correct_login'), b.generate_random_string(8)),
                                                 (b.generate_random_string(8), lazy_fixture('correct_password')),
                                                 (b.generate_random_string(8), b.generate_random_string(8))])
    def test_login_courier_wrong_creds(self, login, password):
        courier = Courier(login, password)
        response = courier.login_courier()
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]
