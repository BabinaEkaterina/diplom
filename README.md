# Тесты на проверку, что по треку заказа можно получить данные о заказе в Яндекс.Самокат с помощью API Яндекс.Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой py -m pytest .\get_order_with_track.py

# SQL-запросы:
1. SELECT c.login, COUNT(o.id) AS orders_in_delivery FROM "Couriers" c JOIN "Orders" o ON c.id = o."courierId" WHERE o."inDelivery" = 't' GROUP BY c.login;
2. SELECT o."track", CASE WHEN o."finished" = 't' THEN 2 WHEN o."cancelled" = 't' THEN -1 WHEN o."inDelivery" = 't' THEN 1 ELSE 0 END AS status FROM "Orders" o;