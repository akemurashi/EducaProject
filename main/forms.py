from django import forms

from .models import apuntes


class formulario_apuntes(forms.ModelForm):
    class Meta:
        model = apuntes
        fields = ("titulo_apunte","informacion_apunte","archivo")
        
        
