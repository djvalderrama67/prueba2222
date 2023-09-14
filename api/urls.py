from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'vehiculo', views.VehiculoViewSet)
router.register(r'bodega', views.BodegaViewSet)
router.register(r'objeto', views.ObjetoViewSet)
router.register(r'calculo', views.CalculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]