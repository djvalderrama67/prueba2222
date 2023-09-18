#from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from django.http import HttpResponse
import pandas as pd
#from import_export.formats import base_formats
#from .resources import *

# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

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

#def export_categorias_to_excel(request):
