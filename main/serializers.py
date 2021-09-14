from rest_framework import serializers
from .models import VINData


class VINDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VINData
        fields = ('vincode', 'year', 'make',
                  'model', 'type', 'state', 'doors')
