# Тело запроса для создания заказа
order_body = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "ул. Ленина, 1",
    "metroStation": "5",
    "phone": "+79995553322",
    "rentTime": 3,
    "deliveryDate": "2023-12-31",
    "comment": "Тестовый заказ",
    "color": ["BLACK"]
}

# Генератор тела запроса с изменяемыми параметрами


def get_order_body(first_name=None, last_name=None, phone=None):
    body = order_body.copy()
    if first_name:
        body["firstName"] = first_name
    if last_name:
        body["lastName"] = last_name
    if phone:
        body["phone"] = phone
    return body
