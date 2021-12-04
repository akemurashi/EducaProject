from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("ramos/", views.Ramos, name="ramos"),
    path("Creacion_ramos/", views.CrearRamos, name = "creacion_ramos"),
    path("lista_ap/<int:id_ramo>", views.lista_apuntes, name="lista_apuntes"),
    path("lista_ap/subir/<int:id_ramo>", views.subir_archivo, name="subir_archivo"),
]
