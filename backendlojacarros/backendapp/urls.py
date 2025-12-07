from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from . import views

router = DefaultRouter()
router.register(r'carros', ItemViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('getCarro', views.getCarro),
    path('saveCarro', views.saveCarro),
    path('deleteCarro', views.deleteCarro),
    path('updateCarro', views.updateCarro),
    path('listarCarros', views.listarCarros),
]
