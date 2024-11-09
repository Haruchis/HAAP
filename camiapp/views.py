
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
from django.urls import reverse_lazy


class CrearLibro(SuccessMessageMixin, CreateView):
    model = libro
    form = libro
    fields = "__all__"
    template_name = 'camiapp/libro_form.html'  # Especifica la plantilla explícitamente
    success_message = 'Libro Creado Correctamente!'
    
    # Define la URL de redirección después de guardar
    def get_success_url(self):
        return reverse_lazy('listar_libros')  # Redirige a la lista de libros

class Listarlibro(ListView):
    model = libro #llamamos a la clase libro que se encuentra en nuestro archivo 'models.py'

class Detallelibro(DetailView):
    model = libro  # llamamos a la clase libro que se encuentra en nuestro archivo 'models.py'
    template_name = "camiapp/detalle_libro.html"  # Especificamos el nombre del template correcto

class Actualizarlibro(SuccessMessageMixin, UpdateView):
    model= libro #llamamos a la clase libro que se encuentra en nuestro archivo 'models.py'
    form = libro  #Definimos nuestro formulario con el nombre de la clase o modelo libro
    fields = "__all__"# le decimos a Django que mmuestre todos los campos de la tabla 'libro'
    success_message = ' Libro Actualizado Correectamente! ' # mostramos este mensaje luego de editarlo

class EliminarLibro(DeleteView):
    model = libro  # El modelo correspondiente
    template_name = "camiapp/eliminar_libro.html"  # Nombre correcto de la plantilla
    success_url = reverse_lazy('listar_libros')  # Redirección después de eliminar

class Inicio(ListView):
    model = libro
    template_name = 'index.html'  # Apunta al archivo de plantilla de inicio
    context_object_name = 'object_list'  # Asegúrate de que el contexto coincida con el usado en la plantilla
