import requests
from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import order_body

# Функция создания нового заказа


def post_new_order(body):
    return requests.post(URL_SERVICE + CREATE_ORDER_PATH, json=body)

# Функция получения заказа по треку


def get_order_by_track(track):
    return requests.get(URL_SERVICE + GET_ORDER_BY_TRACK_PATH, params={"t": track})
