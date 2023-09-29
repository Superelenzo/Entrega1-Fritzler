from django.db import models

# Create your models here.

class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    numero = models.IntegerField()

class Ejemplo(models.Model):
    post = models.CharField(max_length=50)
    texto = models.TextField()
    
 