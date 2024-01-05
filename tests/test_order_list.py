import allure
import requests
from staticdata import Links


class TestOrderList:
    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что в тело ответа возвращается список заказов')
    def test_order_list(self):
        r = requests.get(Links.main + Links.orders)
        orders = r.json()['orders']

        assert r.status_code == 200 and len(orders) > 0
