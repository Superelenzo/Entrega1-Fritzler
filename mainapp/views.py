from django.shortcuts import render, redirect
from datetime import datetime
from django.template import Template, Context, loader
from mainapp.models import Blog
from django.http import HttpResponse
from mainapp.forms import CrearPostFormulario,PostBusquedaFormulario, EditarPostFormulario
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    datos= {
        'fecha': datetime.now()
    }    
    return render(request, r'mainapp/inicio.html', datos)

def about(request):
    return render(request, 'mainapp/about.html')

def crear_post(request):
    
    if request.method == 'POST':
        formulario = CrearPostFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            ejemplo=Blog(post=datos.get('post'), autor= datos['autor'], texto=datos['texto'])
            ejemplo.save()
        else:
            return render(request, r'mainapp/crear_post.html', {'formulario':formulario})
    
    formulario = CrearPostFormulario()
    return render(request, r'mainapp/crear_post.html', {'formulario':formulario})   

def lista_post(request):   
    print(request.GET)
    formulario = PostBusquedaFormulario(request.GET)
    if formulario.is_valid():
        post_buscado = formulario.cleaned_data.get('post')
        post_encontrados = Blog.objects.filter(post__icontains=post_buscado)
        print(post_buscado)
        print(post_encontrados)
    else:
        post_encontrados = Blog.objects.all()
    
    formulario = PostBusquedaFormulario()
    return render(request, r'mainapp/lista_post.html',{'formulario':formulario,'post_encontrados':post_encontrados, 'post_buscado':post_buscado})

@login_required
def editar_post(request, post_id):
    post_a_editar = Blog.objects.get(id=post_id)

    if request.method == 'POST':
        formulario = EditarPostFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            post_a_editar.post = data['post']
            post_a_editar.autor = data['autor']
            post_a_editar.texto = data['texto']
            post_a_editar.save()
            return redirect('posteos')
        else:
            return render(request, 'mainapp/editar_post.html', {'formulario': formulario})
            
    formulario = EditarPostFormulario(initial={'post': post_a_editar.post, 'autor': post_a_editar.autor, 'texto':post_a_editar.texto})
    return render(request, r'mainapp/editar_post.html', {'formulario': formulario})



@login_required
def eliminar_post(request, post_id):
    post_a_eliminar = Blog.objects.get(id=post_id)
    post_a_eliminar.delete()
    
    return redirect('posteos')


def detalles_post(request, post_id):
    post = Blog.objects.get(id=post_id)
    return render(request, 'mainapp/detalles_post.html', {'post': post})
    