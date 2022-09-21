# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404, redirect
from .models import Marca, Modelo, Coche
from .forms import CocheForm, MarcaForm, ModeloForm
from .serializers import CocheSerializer

# Create your views here.

def home_view(request, *args, **kargs):
    return render(request, "home.html", {})

#Listado de marcas
def marcas_view(request, *args, **kargs):
    objetos = Marca.objects.all()
    context = {
        'lista_marcas':objetos     
    }
    return render(request, "marcas.html", context)

#Listado de modelos
def modelos_view(request, *args, **kargs):
    objetos = Modelo.objects.all()
    context = {
        'lista_modelos':objetos     
    }
    return render(request, "modelos.html", context)

# Listado de coches
# Incluye buscador de coches por identificador y filtrado de coches anterior a fecha
def coches_view(request, *args, **kargs):
    #Seleccionar todos los coches de la BD
    objetos = Coche.objects.all()
    #Si entra una request en formato GET
    if request.GET:
        #Inicializar objetos como lista 
        objetos = []
        #Seleccionar los campos rellenos del request 
        fecha = request.GET.get('fecha') or None
        my_id = request.GET.get('id') or None

        #Filtrar / Buscar los datos
        if fecha is not None:
            objetos = Coche.objects.filter(fecha_creacion__lte = fecha)
        if my_id is not None:
            try:
                obj = Coche.objects.get(id=my_id)
                objetos.append(obj)
            except:
                objetos=[]       
    #Pasar el listado de objetos al diccionario para el render
    context = {
        'lista_coches': objetos     
    }
    return render(request, "coches.html", context)

# Funcionalidad para obtener un diccionario en la cual las “keys” deberán de ser todas las
# marcas y los “values” deberán de ser todos los coches de la correspondiente marca.
# Los diccionarios no pueden tener Keys duplicadas por lo que para que tenga sentido se han almacenado como values
# los modelos en una lista por cada marca (Key)
def dictionary_view(request):
    marcas=Marca.objects.all()
    queryset = {}
    for obj_marca in marcas:
        lista_coches=list()
        coches=Coche.objects.filter(marca=obj_marca.id)
        for coche in coches:
            lista_coches.append(str(coche))
        queryset.update({str(obj_marca.nombre):lista_coches})
    context={
        'query':queryset
    }   
    return render(request, "dictionary.html", context)

#Creación de coches
def coche_create_view(request, *args, **kargs):
    #Recolección de datos del formulario
    form = CocheForm(request.POST or None) 
    if form.is_valid():
        form.save()
        #Resetear el formulario
        form = CocheForm()
    context = {
        'form' : form    
    }
    return render(request, "nuevo_coche.html", context)

#Buscador de coches por marca, modelo o ambas
def search_view(request):
    marcas=Marca.objects.all()
    modelos = Modelo.objects.all()
    resultado = []
    if request.GET:
        marca_id = request.GET.get('marca')
        modelo_id = request.GET.get('modelo')

        if marca_id != 'Marca...' and modelo_id != 'Modelo...':
            marca_id = Marca.objects.get(nombre=marca_id).id
            modelo_id = Modelo.objects.get(nombre_modelo=modelo_id).id
            resultado = Coche.objects.filter(marca=marca_id, modelo=modelo_id)
        elif marca_id != 'Marca...':
            marca_id = Marca.objects.get(nombre=marca_id).id
            resultado = Coche.objects.filter(marca=marca_id)
        elif modelo_id != 'Modelo...':
            modelo_id = Modelo.objects.get(nombre_modelo=modelo_id).id
            resultado = Coche.objects.filter(modelo=modelo_id)
    context = {
        'lista_coches' : resultado,
        'marcas':marcas,
        'modelos':modelos
    }
    return render(request, "search.html", context)

# Crear marca
def marca_create_view(request, *args, **kargs):
    form = MarcaForm(request.POST or None) #Recolección de datos del formulario
    if form.is_valid():
        form.save()
        form = MarcaForm()
    context = {
        'form' : form    
    }
    return render(request, "nueva_marca.html", context)

# Crear modelo
def modelo_create_view(request, *args, **kargs):
    form = ModeloForm(request.POST or None) #Recolección de datos del formulario
    if form.is_valid():
        form.save()
        form = ModeloForm()
    context = {
        'form' : form    
    }
    return render(request, "nuevo_modelo.html", context)

# Actualizar coche
def coche_update_view(request, id):
    obj = get_object_or_404(Coche, id=id)
    form = CocheForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("coches/")
    context = {
        'form':form
    }
    return render(request,"coche_update.html", context)

# Actualizar marca
def marca_update_view(request, id):
    obj = get_object_or_404(Marca, id=id)
    form = MarcaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("marcas/")
    context = {
        'form':form
    }
    return render(request,"marca_update.html", context)

# Actualizar modelo
def modelo_update_view(request, id):
    obj = get_object_or_404(Modelo, id=id)
    form = ModeloForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("modelo/")
    context = {
        'form':form
    }
    return render(request,"modelo_update.html", context)

# Borrar coche
def coche_delete_view(request, id):
    obj = get_object_or_404(Coche, id=id)
    #Confirmación del borrado
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {
        'obj':obj
    }
    return render(request,"coche_delete.html", context)

# Borrar marca
def marca_delete_view(request, id):
    obj = get_object_or_404(Marca, id=id)
    #Confirmación del borrado
    if request.method == "POST":
        obj.delete()
        return redirect("marcas/")
    context = {
        'obj':obj
    }
    return render(request,"marca_delete.html", context)

# Borrar modelo
def modelo_delete_view(request, id):
    obj = get_object_or_404(Modelo, id=id)
    #Confirmación del borrado
    if request.method == "POST":
        obj.delete()
        return redirect("modelos/")
    context = {
        'obj':obj
    }
    return render(request,"modelo_delete.html", context)



#API

#Decorador para utilizar vistas basadas en funciones y el método del request
@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'Detail':'api/(?P<id>[0-9]+)',
        'Delete':'api/delete/(?P<id>[0-9]+)',
        'Update':'api/update/(?P<id>[0-9]+)', 
        'Create':'api/create', 
        'List':'api/list',
    }
    return Response(api_urls)

@api_view(['GET'])
def cocheList(request):
    coches = Coche.objects.all().order_by('id')
    serializer = CocheSerializer(coches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cocheDetail(request, id):
    if Coche.objects.filter(id=id).exists():
        coches = Coche.objects.get(id=id)
        serializer = CocheSerializer(coches)
        return Response(serializer.data)
    else: 
        return Response("No existe")

@api_view(['POST'])
def cocheCreate(request):
    serializer = CocheSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def cocheUpdate(request, id):
    if Coche.objects.filter(id=id).exists():
        coche = Coche.objects.get(id=id)
        if request.method == 'GET':
            serializer = CocheSerializer(coche)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CocheSerializer(coche, data = request.data)   
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data) 
            return Response(serializer.errors)
    else:
        return Response("No existe")

@api_view(['GET','DELETE'])
def cocheDelete(request, id):
    if Coche.objects.filter(id=id).exists():
        coche = Coche.objects.get(id=id)
        if request.method == 'GET':
            serializer = CocheSerializer(coche)
            return Response(serializer.data)
        elif request.method == 'DELETE': 
            coche.delete()
            return Response("Objeto eliminado correctamente")
    else:
        return Response("No existe")
