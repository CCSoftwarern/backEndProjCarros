from rest_framework import serializers
from .models import Carros

class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = '__all__'