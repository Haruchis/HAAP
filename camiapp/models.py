from django.db import models
from django.urls import reverse


# Create your models here.
class libro (models.Model):

    libro_id = models.CharField(max_length=200)
    nombre_libro = models.CharField(max_length=200)
    editorial_libro = models.CharField(max_length=200)
    año_libro = models.CharField(max_length=200)
    categoria_libro = models.CharField(max_length=200)
    
def get_absolute_url(self):
    return reverse('detalle_libro', args=[str(self.id)])