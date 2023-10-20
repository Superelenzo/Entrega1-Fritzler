from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioRegistro, FormularioEditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.models import InfoExtra


# Create your views here.
def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username=username, password=password)
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = FormularioRegistro()
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def ver_perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = FormularioEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            info_extra.link = formulario.cleaned_data.get('link')
            info_extra.descripcion = formulario.cleaned_data.get('descripcion')
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.save()
            formulario.save()
            return redirect('ver_perfil')
    else:
        formulario = FormularioEditarPerfil(initial={'link': info_extra.link, 'avatar': info_extra.avatar, 'descripcion': info_extra.descripcion}, instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/editar_pass.html'
    success_url = reverse_lazy('ver_perfil')