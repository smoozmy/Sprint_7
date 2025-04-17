import pytest
import allure
from src import data_api

class TestCreateOrder:

    @pytest.mark.parametrize('colors', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    @allure.title('Создание заказа с разными вариантами цвета')
    def test_create_order_with_colors(self, colors):
        payload = {
            'firstName': 'Иван',
            'lastName': 'Иванов',
            'address': 'Москва, ул. Тестовая, 1',
            'metroStation': 4,
            'phone': '+7 800 555 35 35',
            'rentTime': 5,
            'deliveryDate': '2025-04-20',
            'comment': 'Позвоните за 30 минут',
            'color': colors
        }
        response = data_api.create_order(payload)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        response = data_api.get_orders()
        assert response.status_code == 200
        assert isinstance(response.json().get('orders'), list)
