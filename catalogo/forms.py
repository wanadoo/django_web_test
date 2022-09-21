from django import forms

from .models import *


class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = [
            'marca',
            'modelo',
            'fecha_creacion'
        ]

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields=[
            'nombre'
        ]
    #Controlar que la marca no existe ya
    def clean(self,*args,**kargs):
        print("marca")
        data=self.cleaned_data.get('nombre')
        if Marca.objects.filter(nombre = data):
            raise forms.ValidationError("La marca ya existe")
        return data

        
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields=[
            'nombre_modelo'
        ]
    #Controlar que el modelo no existe ya
    def clean_nombre_modelo(self,*args,**kargs):
        print("modelo")
        nombre=self.cleaned_data.get('nombre_modelo')
        if Modelo.objects.filter(nombre_modelo = nombre):
            raise forms.ValidationError("El modelo ya existe")
        return nombre

