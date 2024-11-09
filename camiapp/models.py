from django.db import models

# Create your models here.
class libro (models.Model):

    libro_id = models.CharField(max_length=200)
    nombre_libro = models.CharField(max_length=200)
    editorial_libro = models.CharField(max_length=200)
    año_libro = models.CharField(max_length=200)
    categoria_libro = models.CharField(max_length=200)