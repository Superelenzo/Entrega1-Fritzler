from django.urls import path
from mainapp.views import about,libro,inicio,shop,crear_post,lista_post, editar_post, eliminar_post, detalles_post, blog_base

urlpatterns = [
    path('',inicio, name='inicio'),
    path('libro/', libro, name='libro'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('posteos/', blog_base, name ='posteos'),
    path('posteos/lista/', lista_post, name= 'lista_post'),
    path('posteos/crear/', crear_post, name='crear_post'),
    path('posteos/<int:post_id>/', detalles_post, name='detalles_post'),
    path('posteos/<int:post_id>/editar/', editar_post, name='editar_post'),
    path('posteos/<int:post_id>/eliminar/', eliminar_post, name='eliminar_post')
]   