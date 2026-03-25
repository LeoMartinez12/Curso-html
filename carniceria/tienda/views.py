# tienda/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'tienda/index.html')

def login(request):
    return render(request, 'tienda/login.html')

def menu_prod(request):
    return render(request, 'tienda/menu_prod.html')

def recomendaciones(request):
    return render(request, 'tienda/recomendaciones.html')

def sucursales(request):
    return render(request, 'tienda/sucursales.html')

def empresa(request):
    return render(request, 'tienda/empresa.html')

# Si quieres una vista específica de productos
def productos(request):
    return render(request, 'tienda/productos.html')