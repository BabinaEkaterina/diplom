# Импорт модуля requests для отправки HTTP-запросов
import requests
# Импорт конфигурационного файла, который содержит настройки URL
import configuration
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CRETAE_ORDER объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных заказа в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CRETAE_ORDER,
                         json=body,
                         headers=data.headers)

def get_order_track(param):
    # GET запрос на получение трека заказа
    print("GET запрос: " + configuration.URL_SERVICE + configuration.ORDER_TRACK + param)
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + param)

def generate_params(param):
    return "?t=" + str(param)