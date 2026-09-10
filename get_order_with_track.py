# Бабина Екатерина, 46-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def create_order():
        order_response = sender_stand_request.post_new_order(data.order_create_body)
        json_respons = order_response.json()
        return json_respons["track"]

def get_order_with_track():
        order_track=create_order()
        param=sender_stand_request.generate_params(order_track)
        get_order=sender_stand_request.get_order_track(param)
        return get_order.status_code


#========================= TEST FUNC ===============================
# Тест 1. Получение заказа по треку заказа
def test_get_order_on_track():
        state=get_order_with_track()
        # Проверяется, что код ответа равен 200
        assert state == 200
