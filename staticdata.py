TEST_ORDER = {
    'firstName': 'Аыва',
    'lastName': 'Дпаофыв',
    'address': 'Лавыаы',
    'metroStation': 2,
    'phone': '+79000000000',
    'rentTime': 2,
    'deliveryDate': '20.12.2023',
    'comment': 'выапваып'
    }


class Links:
    main = 'https://qa-scooter.praktikum-services.ru'
    login = '/api/v1/courier/login'
    courier = '/api/v1/courier/'
    orders = '/api/v1/orders'


class RegistrationData:
    no_login_data = {'login': '', 'password': 'qwerty', 'firstName': 'йцукен'}
    no_password_data = {'login': 'qazwsx', 'password': '', 'firstName': 'йцукен'}


class LoginData:
    no_login_data = {'login': '', 'password': 'qwerty'}
    no_password_data = {'login': 'qwerty', 'password': ''}


