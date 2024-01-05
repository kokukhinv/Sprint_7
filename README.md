# Sprint_7
## Автотесты для API сервиса заказа Самоката ##
В рамках проекта реализованы автотесты для проверки корректной работы API.

## Тесты: ##
### Создание курьера: ###
* _test_create_new_courier_with_unique_creds_ — создание курьера с уникальными данными
* _test_create_new_courier_with_non_complete_creds_ — создание курьера с неполными данными
* _test_create_new_courier_with_non_unique_creds_ — создание курьера с неуникальными данными

### Логин курьера: ###
* _test_authentication_ — вход курьера с верными данными
* _test_login_with_incorrect_cred_ — вход курьера с неверными данными
* _test_login_with_non_complete_creds_ — вход курьера с неполными данными

### Создание заказа: ###
* _test_create_order_with_colors_ — создание заказа с разными цветами

### Список заказов: ###
* _test_order_list_ — получение списка заказов

