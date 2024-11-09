

from django.urls import path
from .views import Listarlibro, Detallelibro, Actualizarlibro, CrearLibro, EliminarLibro, Inicio

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),              # Página de inicio
    path('crear/', CrearLibro.as_view(), name='crear_libro'),         # Ruta para crear un libro
    path('listar/', Listarlibro.as_view(), name='listar_libros'),     # Ruta para listar libros
    path('detalle/<int:pk>/', Detallelibro.as_view(), name='detalle_libro'),  # Ruta para ver detalles de un libro
    path('actualizar/<int:pk>/', Actualizarlibro.as_view(), name='actualizar_libro'), # Ruta para actualizar un libro
    path('eliminar/<int:pk>/', EliminarLibro.as_view(), name='eliminar_libro'),  # Ruta para eliminar un libro
]
