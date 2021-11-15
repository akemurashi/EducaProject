from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
def home(response):
    return render(response,"main/home.html",{})