from django.http import JsonResponse
from django.shortcuts import render  # Importa render para las plantillas

def obtener_datos(request):
    # Datos de ejemplo
    datos = {
        "etiquetas": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "valores": [12, 19, 3, 5, 2, 3]
    }
    return JsonResponse(datos)

def mostrar_grafica(request):
    # Renderiza la plantilla HTML
    return render(request, 'graficas/mi_grafica.html')
