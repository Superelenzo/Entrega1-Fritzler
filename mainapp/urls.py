from django.urls import path
from mainapp.views import inicio,crear_post,lista_post

urlpatterns = [
    path('',inicio, name='inicio'),
    path('crear',crear_post, name='crear_post'),
    path('post',lista_post, name='post')
]   