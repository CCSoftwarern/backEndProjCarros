from rest_framework import viewsets
from .models import Carros
from .serializers import CarrosSerializer

class ItemViewSet(viewsets.ModelViewSet):  # Certifique-se de que está usando a classe corretamente
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer

