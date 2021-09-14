from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .views import CreateVin
from .models import VINData

# Create your tests here.


class VinTest(TestCase):
    def setUp(self) -> None:
        self.instance = CreateVin()
        self.factory = APIRequestFactory()

    def test_get_vin_api(self):
        vin = '1P3EW65F4VV300946'
        request = self.factory.get('', data={'vin': vin})
        res = self.instance.get(request=request, vin=vin)
        vin_data = VINData.objects.filter(vincode=vin)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(vin_data.exists())
