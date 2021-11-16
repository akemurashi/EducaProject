from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import EncuestaRegistro
# Create your views here.
def register(response):
    if response.method == "POST":
        form = EncuestaRegistro(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = EncuestaRegistro()    
    return render(response, "usuarios/register.html", {"form":form})