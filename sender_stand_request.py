# Импорт модуля requests для отправки HTTP-запросов
import requests
# Импорт конфигурационного файла, который содержит настройки URL
import configuration
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Функция для создания курьеров
def post_create_courier(body):
    # Выполняет POST-запрос создания курьера в БД
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_COURIER,
                        headers=data.headers,
                        json=body)

def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CRETAE_ORDER объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных заказа в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CRETAE_ORDER,
                         json=body,
                         headers=data.headers)

def put_order_state(param):
    # PUT запрос на изменение статуса заказа inDelivery (принят)
    return requests.put(configuration.URL_SERVICE + configuration.ORDER_STATE + param)

def put_order_finish(param):
    # PUT запрос на изменение статуса заказа finished (завершен)
    return requests.put(configuration.URL_SERVICE + configuration.ORDER_FINISH + param)

def put_order_cancel(param):
    # PUT запрос на изменение статуса заказа cancelled (отменен)
    return requests.put(configuration.URL_SERVICE + configuration.ORDER_CANCEL + param)

def get_order_track(param):
    # GET запрос на получение трека заказа
    print("GET запрос: " + configuration.URL_SERVICE + configuration.ORDER_TRACK + param)
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + param)

def generate_params(param):
    return "?t=" + str(param)