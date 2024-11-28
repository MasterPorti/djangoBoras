from django.urls import path
from .views import obtener_datos, mostrar_grafica

urlpatterns = [
    path('graficas/', obtener_datos, name='obtener_datos'),
    path('mostrar-grafica/', mostrar_grafica, name='mostrar_grafica'),
]
