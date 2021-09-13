from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import VINData


class VINSerializer(serializers.ModelSerializer):
    class Meta:
        model = VINData
        fields = '__all__'
