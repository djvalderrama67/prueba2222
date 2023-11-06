from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action  # Agrega esta línea para importar action
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Categoria': '/categoria/',
        'Vehiculo': '/vehiculo/',
        'Bodega': '/bodega/',
        'Objeto': '/objeto/',
        'Objetos por categoria': '/categoria/<str:nombre_categoria>/',
        'Calculo': '/calculo/',
    }
    return Response(api_urls)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def objetos_por_categoria(self, request, nombre_categoria=None):  # Recibe el parámetro nombre_categoria
        try:
            categoria = Categoria.objects.get(nombre=nombre_categoria)  # Obtén la categoría por su nombre
            objetos = Objeto.objects.filter(categoria=categoria)
            serializer = ObjetoSerializer(objetos, many=True)
            return Response(serializer.data)
        except Categoria.DoesNotExist:
            return Response({"message": "Categoría no encontrada"}, status=status.HTTP_404_NOT_FOUND)



class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer

class ObjetoViewSet(viewsets.ModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer

class CalculoViewSet(viewsets.ModelViewSet):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer


