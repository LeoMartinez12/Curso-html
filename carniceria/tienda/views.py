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

def productos(request):
    return render(request, 'tienda/productos.html')

    # Simulación de base de datos
USERS = []

from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        for user in USERS:
            if user["username"] == username and user["password"] == password:
                request.session["user"] = username
                return redirect("index")

        return render(request, "tienda/login.html", {"error": "Credenciales incorrectas"})

    return render(request, "tienda/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar si ya existe
        for user in USERS:
            if user["username"] == username:
                return render(request, "tienda/registro.html", {"error": "Usuario ya existe"})

        USERS.append({
            "username": username,
            "password": password
        })

        return redirect("login")

    return render(request, "tienda/registro.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")