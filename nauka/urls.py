from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/nowa/', views.nowa_lista, name='nowa_lista'),
    path('lista/<int:lista_id>/', views.lista_slowek, name='lista_slowek'),
]