import json
import pytest
import allure
import requests
from staticdata import Links, TEST_ORDER


class TestCreateOrder:

    @allure.title('Создание заказа с разными цветами')
    @allure.description('Проверка, что можно указать один из цветов — BLACK, GREY или оба')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREY'], ''])
    def test_create_order_with_colors(self, color):
        TEST_ORDER['color'] = color
        data = json.dumps(TEST_ORDER)
        r = requests.post(Links.main + Links.orders, data=data)

        assert r.status_code == 201 and 'track' in r.text
