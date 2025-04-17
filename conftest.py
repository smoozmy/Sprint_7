import pytest
from src import data_api
from src.data_generator import generate_courier

@pytest.fixture
def registered_courier():
    courier = generate_courier()
    data_api.create_courier(courier)
    yield courier
    login_resp = data_api.login_courier({
        'login': courier['login'],
        'password': courier['password']
    })
    courier_id = login_resp.json().get('id')
    data_api.delete_courier(courier_id)