# tienda/urls.py
# tienda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu_prod, name='menu'),
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('empresa/', views.empresa, name='empresa'),
    path('productos/', views.menu_prod, name='productos'),  # <- aquí cambias menu_prod por productos
]