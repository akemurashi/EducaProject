from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("ramos/", views.Ramos, name="ramos"),
    path("Creacion_ramos/", views.CrearRamos, name = "creacion_ramos")
]
