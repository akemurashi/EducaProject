from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ramos_usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_ramo = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre_ramo = models.CharField(max_length=200)
    sigla_ramo = models.CharField(max_length=10)
    foto_ramo = models.CharField(max_length=200)
    