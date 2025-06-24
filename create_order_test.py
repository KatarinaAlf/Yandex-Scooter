# Екатерина Альфирова, 31-я когорта - Финальный проект. Инженер по тестированию плюс.

import sender_stand_request
import data

# Тест 1: Успешное создание заказа и проверка по треку


def test_create_order_and_check_by_track_success():
    # Создаем заказ
    order_response = sender_stand_request.post_new_order(data.order_body)
    assert order_response.status_code == 201, "Ошибка при создании заказа"

    # Получаем трек-номер
    track = order_response.json().get("track")
    assert track is not None, "Трек-номер не получен"

    # Проверяем заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, "Ошибка при получении заказа"
    assert get_response.json().get("order") is not None, "Данные заказа не получены"


