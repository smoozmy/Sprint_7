import pytest
import allure
from src import data_api

class TestLoginCourier:

    @allure.title('Успешный логин курьера с валидными данными')
    def test_login_courier_success(self, registered_courier):
        login_payload = {
            'login': registered_courier['login'],
            'password': registered_courier['password']
        }
        response = data_api.login_courier(login_payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Ошибка при логине с неверным паролем')
    def test_login_courier_wrong_password(self, registered_courier):
        login_payload = {
            'login': registered_courier['login'],
            'password': 'wrong password'
        }
        response = data_api.login_courier(login_payload)
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in response.text

    @pytest.mark.parametrize('login_courier, password_courier', [
        ('some_login', ''),
        ('', 'some_password')
    ])
    @allure.title('Ошибка при логине без логина или пароля')
    def test_login_courier_missing_fields(self, login_courier, password_courier):
        payload = {'login': login_courier, 'password': password_courier}
        response = data_api.login_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'
