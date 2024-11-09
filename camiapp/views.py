
from django.shortcuts import render
from .models import libro
#Iniciamos las vistas genericas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#nos sirve para redireccionar despues de una accion revertiendo patrones de expresion regulares
from django.urls import reverse

#habilitamos el uso de mensajes en Django
from django.contrib import messages

#habilitamos los mensajes para class.based vies
from django.contrib.messages.views import SuccessMessageMixin

# habilitamos los formularios en Django
from django import forms

class CrearLibro(SuccessMessageMixin, CreateView):
    model = libro 
    form = libro 
     
    fields = "__all__"
    success_message = ' Libro Creado Correctamente !'

class Listarlibro(ListView):
    model = libro #llamamos a la clase libro que se encuentra en nuestro archivo 'models.py'

class Detallelibro(DetailView):
    model = libro # llamamos a la clase libro que se encuentra en nuestro arcvhivo 'models.py'

class Actualizarlibro(SuccessMessageMixin, UpdateView):
    model= libro #llamamos a la clase libro que se encuentra en nuestro archivo 'models.py'
    form = libro  #Definimos nuestro formulario con el nombre de la clase o modelo libro
    fields = "__all__"# le decimos a Django que mmuestre todos los campos de la tabla 'libro'
    success_message = ' Libro Actualizado Correectamente! ' # mostramos este mensaje luego de editarlo

class EliminarLibro(SuccessMessageMixin, DeleteView):
    model = libro
    form = libro
    slug_field = "__all__"
def get_success_url(self):
    success_message = ' Libro Eliminado Correctamente !' #mostramos este mensaje luego de eliminarlos
    messages.success (self.request, (success_message))
    return reverse('leer') # redireccionamos a la vista principal 'leer'