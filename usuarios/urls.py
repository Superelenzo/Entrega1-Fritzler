from django.urls import path
from usuarios.views import login, registro, ver_perfil, editar_perfil, CambiarContrasenia
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('registrarse/', registro, name='registro'),
    path('perfil/' ,ver_perfil, name='ver_perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/contraseña/', CambiarContrasenia.as_view(), name='editar_pass'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
