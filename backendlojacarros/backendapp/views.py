from rest_framework import viewsets
from .models import Carros
from .serializers import CarrosSerializer
from django.http import HttpResponse
from django.shortcuts import render

class ItemViewSet(viewsets.ModelViewSet):  # Certifique-se de que está usando a classe corretamente
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carros
from .serializers import CarrosSerializer

# POST - getCarro (entrada: modelo / saída: preço)
# @api_view(['POST'])
# def getCarro(request):
#     modelo = request.data.get("modelo")
#     try:
#         carro = Carros.objects.get(modelo=modelo)
#         return Response({"preco": carro.preco})
#     except Carros.DoesNotExist:
#         return Response({"erro": "Carro não encontrado"}, status=404)


@api_view(['POST'])
def getCarro(request):
    try:
        # Entrada: texto puro
        modelo = request.body.decode('utf-8').strip()

        if not modelo:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        carro = Carros.objects.get(modelo=modelo)

        # Saída: texto puro (preço)
        return HttpResponse(
            str(carro.preco),
            content_type="text/plain",
            status=status.HTTP_200_OK
        )

    except Carros.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


# POST - saveCarro (entrada: modelo, preco / saída: nenhuma)
# @api_view(['POST'])
# def saveCarro(request):
#     serializer = CarrosSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=400)


@api_view(['POST'])
def saveCarro(request):
    # Lê o corpo como texto puro
    body = request.body.decode('utf-8')  # ex: "BMW,350000"

    try:
        modelo, preco = body.split(',')
        preco = float(preco)

        Carros.objects.create(
            modelo=modelo.strip(),
            preco=preco
        )

        # Resposta SEM corpo
        return HttpResponse(status=status.HTTP_201_CREATED)

    except Exception:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


# POST - deleteCarro (entrada: modelo / saída: nenhuma)
# @api_view(['POST'])
# def deleteCarro(request):
#     modelo = request.data.get("modelo")
#     try:
#         carro = Carros.objects.get(modelo=modelo)
#         carro.delete()
#         return Response(status=200)
#     except Carros.DoesNotExist:
#         return Response({"erro": "Carro não encontrado"}, status=404)


@api_view(['POST'])
def deleteCarro(request):
    try:
        # Lê o corpo como texto puro
        modelo = request.body.decode('utf-8').strip()

        if not modelo:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        carro = Carros.objects.get(modelo=modelo)
        carro.delete()

        # Sem body
        return HttpResponse(status=status.HTTP_200_OK)

    except Carros.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


# POST - updateCarro (entrada: modelo, preco / saída: nenhuma)
# @api_view(['POST'])
# def updateCarro(request):
#     modelo = request.data.get("modelo")
#     preco = request.data.get("preco")

#     try:
#         carro = Carros.objects.get(modelo=modelo)
#         carro.preco = preco
#         carro.save()
#         return Response(status=200)
#     except Carros.DoesNotExist:
#         return Response({"erro": "Carro não encontrado"}, status=404)


@api_view(['POST'])
def updateCarro(request):
    try:
        # Corpo da requisição: "BMW,375000"
        body = request.body.decode('utf-8').strip()

        if ',' not in body:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        modelo, preco = body.split(',', 1)
        modelo = modelo.strip()
        preco = float(preco.strip())

        carro = Carros.objects.get(modelo=modelo)
        carro.preco = preco
        carro.save()

        # Resposta sem body
        return HttpResponse(status=status.HTTP_200_OK)

    except Carros.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        # Erro ao converter preço
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    except Exception:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


# POST - listarCarros (entrada: nenhuma / saída: lista)
@api_view(['GET'])
def listarCarros(request):
    carros = Carros.objects.all()
    serializer = CarrosSerializer(carros, many=True)
    return Response(serializer.data)


def index(request):
    return render(request, 'index.html') # index.html deve estar na pasta templates