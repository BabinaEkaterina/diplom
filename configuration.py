# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = "https://2aca108c-856e-4f22-b0b1-bb07a4ae5ca5.serverhub.praktikum-services.ru"
CREATE_COURIER = "/api/v1/courier"          # POST
CRETAE_ORDER = "/api/v1/orders"             # POST
ORDER_STATE = "/api/v1/orders/accept"       # PUT /{orderId}?courierId={id}
ORDER_FINISH = "/api/v1/orders/finish"      # PUT /{orderId}
ORDER_CANCEL = "/api/v1/orders/cancel"      # PUT ?track={num}
ORDER_TRACK = "/api/v1/orders/track"        # GET /track?t={num}