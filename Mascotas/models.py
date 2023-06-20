from django.db import models

# Create your models here.

class Productos(models.Model):
    dv = models.CharField(primary_key=True,max_length=5,verbose_name="Dv")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.pk