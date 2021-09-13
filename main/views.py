from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import requests


@api_view(['GET'])
def view_vins(request):
    if request.method == 'GET':
        vin_data = VINData.objects.all()
        serializer = VINSerializer(vin_data)
        return Response(serializer.data)
    return Response()


@api_view(['GET'])
def get_vin(request, vin=None):
    if request.method == 'GET':
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
            vin_data = VINSerializer(vincode=vin)

        return Response(vin_data.data)

    return Response()
