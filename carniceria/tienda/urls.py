from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_prod, name='menu'),
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('empresa/', views.empresa, name='empresa'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.register_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]