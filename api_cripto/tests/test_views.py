import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from app_cripto.models import CriptoModel

pytestmark = pytest.mark.django_db


class TestCriptoListApi(TestCase):

    @classmethod
    def setUp(self):
        self.client = APIClient()
        print(self.client, 'self.client')

    def test_cripto_list_work(self):

        url = reverse('cripto_list_api')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        assert response.json() != None



    def test_cripto_create_work(self):

        input_data = {
            'name': 'Test',
            'symbol': 'TST',
            'price': 2.2,
            'percent_change_24h': 2.3,
            'volume_24h': 1.2,
            'volume_change_24h': 1.3
        }

        url = reverse('cripto_list_api')
        response = self.client.post(url, data=input_data)

        print(response.data)

        assert response.json() != None
        self.assertEqual(CriptoModel.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

class TestCriptoDetailApi(TestCase):

    @classmethod
    def setUp(self):
        self.client = APIClient()
        coin_1 = CriptoModel.objects.create(
                name='Test1', symbol='TS1', price=2.2, percent_change_24h=2.3,
                volume_24h=1.2, volume_change_24h=1.3
        )
        coin_1.save()
        coin_2 = CriptoModel.objects.create(
            name='Test2', symbol='TS2', price=2.2, percent_change_24h=2.3,
            volume_24h=1.2, volume_change_24h=1.3
        )
        coin_2.save()
        print(self.client, 'self.client')

    def test_cripto_detail_work(self):

        url_1 = reverse('cripto_detail', kwargs={'pk': 1})
        url_2 = reverse('cripto_detail', kwargs={'pk': 2})
        response_1 = self.client.get(url_1)
        response_2 = self.client.get(url_2)

        print(response_1.json(), 'response_1 json')
        assert response_1.json() != None
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1.json()['name'], 'Test1')
        self.assertEqual(response_1.json()['symbol'], 'TS1')

        print(response_2.json(), 'response_2 json')
        assert response_2.json() != None
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_2.json()['name'], 'Test2')
        self.assertEqual(response_2.json()['symbol'], 'TS2')

    def test_cripto_delete_work(self):

        self.assertEqual(CriptoModel.objects.count(), 2)
        url = reverse('cripto_detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(CriptoModel.objects.count(), 1)

    def test_cripto_update_work(self):

        coin = CriptoModel.objects.get(id=1)
        url = reverse('cripto_detail', kwargs={'pk': 3})
        response = self.client.put(url)
        self.assertEqual(coin.symbol, 'TS1')
        coin.symbol = 'TST'
        coin.save()
        self.assertEqual(coin.symbol, 'TST')





