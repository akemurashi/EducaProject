from django.contrib import admin
from .models import apuntes, ramos_usuario
# Register your models here.
admin.site.register(ramos_usuario)
admin.site.register(apuntes)