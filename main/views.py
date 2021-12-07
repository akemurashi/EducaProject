from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.http.response import HttpResponseRedirect
from .models import ramos_usuario, apuntes
from django.templatetags.static import static
from .forms import formulario_apuntes
# Create your views here.
def home(response):
    return render(response,"main/home.html",{})

def Ramos(response):
    choices=[(0,static("images/bio1.jpg")), (1,static("images/bio2.jpg")), (2,static("images/efi1.jpg"))]
    context = {"informacion_ramos":ramos_usuario.objects.filter(usuario_ramo=response.user),"foto_ramo_h":choices,"nombre_del_usuario":response.user}
    return render(response, "main/ramos_usuario.html",context)

def CrearRamos(response):
    choices=[static("images/bio1.jpg"), static("images/bio2.jpg"), static("images/efi1.jpg"), static("images/efi2.jpg"), static("images/filo1.jpg")
            , static("images/intro2.jpg"), static("images/mat2.jpg"), static("images/mat3.jpg"), static("images/qui1.jpg"), static("images/qui2.jpg"), static("images/qui3.jpg")]
    if response.method == "POST":
        form = response.POST
        nuevo_ramo = ramos_usuario()
        nuevo_ramo.usuario_ramo = response.user
        nuevo_ramo.nombre_ramo = form["n_ramo"]
        nuevo_ramo.sigla_ramo = form["sigla_ramo"]
        nuevo_ramo.foto_ramo = form["imagen"]
        nuevo_ramo.save()
        return redirect('ramos')
    return render(response, "main/Creacion_ramos.html", {"images":choices})


def lista_apuntes(request,id_ramo):
    ramo = ramos_usuario.objects.get(pk=id_ramo)
    todos_apuntes = apuntes.objects.all().filter(ramo_apunte=ramo)
    return render(request,'main/lista_apuntes.html', {'todos_los_apuntes':todos_apuntes,"ramo":ramo})

def subir_archivo(request,id_ramo):
    if request.method == "POST":
        form = formulario_apuntes(request.POST, request.FILES)
        if form.is_valid():
            form=form.cleaned_data
            apunte = apuntes()
            apunte.titulo_apunte=form["titulo_apunte"]
            apunte.informacion_apunte=form["informacion_apunte"]
            apunte.archivo=form["archivo"]
            apunte.ramo_apunte=ramos_usuario.objects.get(pk=id_ramo)
            apunte.save()
            return redirect('/lista_ap/'+str(id_ramo))
    else:
        form = formulario_apuntes()
    form = formulario_apuntes()
    return render(request,'main/subir_archivo.html', {'form':form})
