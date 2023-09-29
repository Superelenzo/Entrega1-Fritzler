from django.shortcuts import render
from datetime import datetime
from mainapp.models import Curso

# Create your views here.

def inicio(request):
    datos= {
        'fecha': datetime.now()
    }    
    return render(request, r'mainapp\inicio.html', datos)
def crear_curso(request,titulo,numero):
    curso = Curso(titulo = titulo, numero=numero)
    curso.save()
    
    return(render(request, r'mainapp\curso_creado.html', {}))