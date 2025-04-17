import requests

BASE_URL = 'https://qa-scooter.praktikum-services.ru'

def create_courier(payload):
    return requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

def login_courier(payload):
    return requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

def delete_courier(courier_id):
    return requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')

def create_order(payload):
    return requests.post(f'{BASE_URL}/api/v1/orders', json=payload)

def get_orders():
    return requests.get(f'{BASE_URL}/api/v1/orders')