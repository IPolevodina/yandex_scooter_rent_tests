import configuration
import requests
import data

# Получение номера трека из ответа по запросу на создание заказа
def create_order_and_get_track():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.create_order_body)
    return response.json()['track']

# Получение заказа по номеру трека
def get_order_by_id(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t": track} )
