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
    path('menu_prod/', views.menu_prod, name='productos'),  # URL de productos
]