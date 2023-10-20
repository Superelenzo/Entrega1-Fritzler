from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    post = models.CharField(max_length=50)
    autor = models.CharField(max_length=50, default='')
    texto = RichTextField()
    
    def __str__(self):
        return f'{self.post}'
