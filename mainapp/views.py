from django.shortcuts import render
from datetime import datetime
from mainapp.models import Blog
from mainapp.forms import PostFormulario,BusquedaFormulario

# Create your views here.

def inicio(request):
    datos= {
        'fecha': datetime.now()
    }    
    return render(request, r'mainapp\inicio.html', datos)

def crear_post(request):
    
   # print(request.POST)
    if request.method == 'POST':
        formulario = PostFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            ejemplo=Blog(post=datos.get('post'), autor= datos['autor'], texto=datos['texto'])
            ejemplo.save()
        else:
            return render(request, r'mainapp\crear_post.html', {'formulario':formulario})
    
    formulario = PostFormulario()
    return render(request, r'mainapp\crear_post.html', {'formulario':formulario})   

def lista_post(request):   
    print(request.GET)
    formulario = BusquedaFormulario(request.GET)
    if formulario.is_valid():
        post_buscado = formulario.cleaned_data.get('post')
        post_encontrados = Blog.objects.filter(post__icontains=post_buscado)
        print(post_buscado)
        print(post_encontrados)
    else:
        post_encontrados = Blog.objects.all()
    
    formulario = BusquedaFormulario()
    return render(request, r'mainapp\lista_post.html',{'formulario':formulario,'post_encontrados':post_encontrados, 'post_buscado':post_buscado})
