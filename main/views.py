from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VINDataSerializer
from .models import VINData
import requests


class CreateVin(APIView):
    """
    APIView for getting the decoded data for Vehicle ID 
    EndPoint receives the VIN -> decodes -> stores on DB
    """

    def get(self, request, vin=None):
        vin_data = VINDataSerializer(VINData.objects.all(), many=True)
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
        res = requests.post(url, data={'format': 'json', 'data': vin})

        if res.status_code == 200:
            json_data = res.json()['Results'][0]
            make = json_data['Make']
            doors = json_data['Doors']
            model = json_data['Model']
            model_year = json_data['ModelYear']
            state = json_data['PlantState']
            type = json_data['VehicleType']

            # Store decoded values
            if not VINData.objects.filter(vincode=vin).exists():
                VINData.objects.create(
                    vincode=vin,
                    year=model_year,
                    make=make,
                    model=model,
                    type=type,
                    state=state,
                    doors=doors
                )
                #vin = VINData.objects.get(vincode=vin)
            #vin_data = VINSerializer(vin)

        return Response(vin_data.data)
