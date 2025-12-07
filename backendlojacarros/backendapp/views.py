from rest_framework import viewsets
from .models import Carros
from .serializers import CarrosSerializer

class ItemViewSet(viewsets.ModelViewSet):  # Certifique-se de que está usando a classe corretamente
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carros
from .serializers import CarrosSerializer

# POST - getCarro (entrada: modelo / saída: preço)
@api_view(['POST'])
def getCarro(request):
    modelo = request.data.get("modelo")
    try:
        carro = Carros.objects.get(modelo=modelo)
        return Response({"preco": carro.preco})
    except Carros.DoesNotExist:
        return Response({"erro": "Carro não encontrado"}, status=404)


# POST - saveCarro (entrada: modelo, preco / saída: nenhuma)
@api_view(['POST'])
def saveCarro(request):
    serializer = CarrosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)


# POST - deleteCarro (entrada: modelo / saída: nenhuma)
@api_view(['POST'])
def deleteCarro(request):
    modelo = request.data.get("modelo")
    try:
        carro = Carros.objects.get(modelo=modelo)
        carro.delete()
        return Response(status=200)
    except Carros.DoesNotExist:
        return Response({"erro": "Carro não encontrado"}, status=404)


# POST - updateCarro (entrada: modelo, preco / saída: nenhuma)
@api_view(['POST'])
def updateCarro(request):
    modelo = request.data.get("modelo")
    preco = request.data.get("preco")

    try:
        carro = Carros.objects.get(modelo=modelo)
        carro.preco = preco
        carro.save()
        return Response(status=200)
    except Carros.DoesNotExist:
        return Response({"erro": "Carro não encontrado"}, status=404)


# POST - listarCarros (entrada: nenhuma / saída: lista)
@api_view(['POST'])
def listarCarros(request):
    carros = Carros.objects.all()
    serializer = CarrosSerializer(carros, many=True)
    return Response(serializer.data)


