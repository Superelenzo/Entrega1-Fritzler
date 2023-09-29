from django.urls import path
from mainapp.views import inicio,crear_curso



urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-curso/<str:titulo>/<int:numero>',crear_curso, name='crear_curso')
     
]