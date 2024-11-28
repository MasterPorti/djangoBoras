from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('graficas.urls')),  # Incluir las rutas de la app 'graficas'
]
