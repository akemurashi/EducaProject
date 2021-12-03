from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, request
from django.http.response import HttpResponseRedirect
from .models import ramos_usuario
from django.templatetags.static import static

# Create your views here.
def home(response):
    return render(response,"main/home.html",{})

def Ramos(response):
    choices=[(0,static("images/bio1.jpg")), (1,static("images/bio2.jpg")), (2,static("images/efi1.jpg"))]
    context = {"informacion_ramos":ramos_usuario.objects.filter(usuario_ramo=response.user),"foto_ramo_h":choices,"nombre_del_usuario":response.user}
    return render(response, "main/ramos_usuario.html",context)

def CrearRamos(response):
    choices=[static("images/bio1.jpg"), static("images/bio2.jpg"), static("images/efi1.jpg")]
    if response.method == "POST":
        form = response.POST
        nuevo_ramo = ramos_usuario()
        nuevo_ramo.usuario_ramo = response.user
        nuevo_ramo.nombre_ramo = form["n_ramo"]
        nuevo_ramo.sigla_ramo = form["sigla_ramo"]
        nuevo_ramo.foto_ramo = form["imagen"]
        nuevo_ramo.save()
    return render(response, "main/Creacion_ramos.html", {"images":choices})
