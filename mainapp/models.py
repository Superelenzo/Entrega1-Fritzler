from django.db import models

# Create your models here.

class Blog(models.Model):
    post = models.CharField(max_length=50)
    autor = models.CharField(max_length=50, default='')
    texto = models.TextField()
    
    def __str__(self):
        return f'- Post: {self.post} - Autor: {self.autor} - Texto: {self.texto}'
