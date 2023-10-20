from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Movil(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = RichTextField()
    fecha_lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to='galeria', null=True, blank=True)
    
    def __str__(self):
        return f'{self.marca} {self.modelo}'