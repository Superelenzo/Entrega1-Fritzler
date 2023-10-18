from django.urls import path
from productapp import views


urlpatterns = [
    path('productos/', views.MovilBaseView.as_view(), name='productos'),
    path('productos/lista/', views.MovilListView.as_view(), name='listar_movil'),
    path('productos/crear/', views.MovilCreateView.as_view(), name='crear_movil'),
    path('productos/<int:pk>/', views.MovilDetailView.as_view(), name='detalle_movil'),
    path('productos/<int:pk>/editar/', views.MovilUpdateView.as_view(), name='editar_movil'),
    path('productos/<int:pk>/eliminar/', views.MovilDeleteView.as_view(), name='eliminar_movil'),
]