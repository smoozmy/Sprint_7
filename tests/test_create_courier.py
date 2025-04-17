import pytest
import allure
from src import data_api
from src.data_generator import generate_courier


class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными')
    def test_create_courier_success(self):
        with allure.step('Генерация данных курьера'):
            courier = generate_courier()
        with allure.step('Отправка запроса на создание курьера'):
            response = data_api.create_courier(courier)
        with allure.step('Проверка успешного создания'):
            assert response.status_code == 201
            assert response.json()['ok'] is True
        with allure.step('Удаление тестового курьера'):
            login_resp = data_api.login_courier({
                'login': courier['login'],
                'password': courier['password']
            })
            courier_id = login_resp.json().get('id')
            data_api.delete_courier(courier_id)

    @allure.title('Создание курьера с уже существующим логином')
    def test_create_courier_duplicate(self):
        courier = generate_courier()
        data_api.create_courier(courier)
        with allure.step('Повторная попытка создания того же курьера'):
            duplicate_response = data_api.create_courier(courier)
            assert duplicate_response.status_code == 409
            assert 'Этот логин уже используется' in duplicate_response.text
        login_resp = data_api.login_courier({
            'login': courier['login'],
            'password': courier['password']
        })
        courier_id = login_resp.json().get('id')
        data_api.delete_courier(courier_id)

    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    @allure.title('Создание курьера с пропущенным обязательным полем')
    def test_create_courier_missing_required_field(self, missing_field):
        courier = generate_courier()
        del courier[missing_field]
        response = data_api.create_courier(courier)
        assert response.status_code == 400
        assert 'Недостаточно данных' in response.text
