from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
def home(response):
    print(response.user)
    return render(response,"main/home.html",{})
def Ramos(response):
    context = {}
    return render(response, "main/ramos_usuario.html",context)