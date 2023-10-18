from django.urls import path
from mainapp.views import about,inicio,crear_post,lista_post, editar_post, eliminar_post, detalles_post

urlpatterns = [
    path('',inicio, name='inicio'),
    path('about/', about, name='about'),
    path('posteos/', lista_post, name='posteos'),
    path('posteos/crear/', crear_post, name='crear_post'),
    path('posteos/<int:post_id>/', detalles_post, name='detalles_post'),
    path('posteos/<int:post_id>/editar/', editar_post, name='editar_post'),
    path('posteos/<int:post_id>/eliminar/', eliminar_post, name='eliminar_post')
]   