# views.py
from django.shortcuts import render, redirect

# Simulación de base de datos en memoria
USERS = []

# =====================
# LOGIN
# =====================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Buscar usuario en USERS
        for user in USERS:
            if user["username"] == username and user["password"] == password:
                request.session["user"] = username  # Guardar sesión
                return redirect("index")

        return render(request, "tienda/login.html", {"error": "Credenciales incorrectas"})

    return render(request, "tienda/login.html")


# =====================
# REGISTRO
# =====================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar si ya existe
        for user in USERS:
            if user["username"] == username:
                return render(request, "tienda/login.html", {"error": "Usuario ya existe"})

        # Agregar nuevo usuario
        USERS.append({
            "username": username,
            "password": password
        })

        request.session["user"] = username  # Loguear automáticamente
        return redirect("index")

    return render(request, "tienda/login.html")


# =====================
# LOGOUT
# =====================
def logout_view(request):
    request.session.flush()  # Borra la sesión
    return redirect("login")


# =====================
# VISTAS PRINCIPALES
# =====================
def index(request):
    if "user" not in request.session:
        return redirect("login")
    return render(request, "tienda/index.html")


def menu_prod(request):
    if "user" not in request.session:
        return redirect("login")
    return render(request, "tienda/menu_prod.html")  # <-- coincide con el nombre real

def recomendaciones(request):
    if "user" not in request.session:
        return redirect("login")
    return render(request, "tienda/recomendaciones.html")


def sucursales(request):
    if "user" not in request.session:
        return redirect("login")
    return render(request, "tienda/sucursales.html")


def empresa(request):
    if "user" not in request.session:
        return redirect("login")
    return render(request, "tienda/empresa.html")