# Тестирование API создания заказов Яндекс Самокат

Проект содержит автотесты для проверки:
- Создания заказов через `/api/v1/orders`
- Получения данных заказа по треку через `/api/v1/orders/track`

## Структура проекта
- `configuration.py` - настройки URL API
- `data.py` - тестовые данные
- `sender_stand_request.py` - функции для отправки запросов
- `create_order_test.py` - тестовые сценарии

## Запуск тестов
```bash
pytest create_order_test.py -v