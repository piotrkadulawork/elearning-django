from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/nowa/', views.nowa_lista, name='nowa_lista'),
    path('lista/<int:lista_id>/', views.lista_slowek, name='lista_slowek'),
    path('slowko/<int:slowko_id>/usun/', views.usun_slowko, name='usun_slowko'),
    path('slowko/<int:slowko_id>/edytuj/', views.edytuj_slowko, name='edytuj_slowko'),
    path('lista/<int:lista_id>/edytuj/', views.edytuj_liste, name='edytuj_liste'),
    path('lista/<int:lista_id>/usun/', views.usun_liste, name='usun_liste'),
]