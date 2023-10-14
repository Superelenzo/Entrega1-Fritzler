from django.shortcuts import render

# Create your views here.

from productapp.models import Movil

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MovilCreateView(CreateView):
    model = Movil
    template_name = "productapp/crear_movil.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_lanzamiento']
    success_url = reverse_lazy('productos')


class MovilDeleteView(LoginRequiredMixin, DeleteView):
    model = Movil
    template_name = "productapp/eliminar_movil.html"
    success_url = reverse_lazy('productos')


class MovilDetailView(DetailView):
    model = Movil
    template_name = "productapp/detalle_movil.html"


class MovilListView(ListView):
    model = Movil
    context_object_name = 'listado_movil'
    template_name = "productapp/listar_movil.html"
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            paletas = self.model.objects.filter(marca__icontains=marca)
        else:
            paletas = self.model.objects.all()
        return paletas

class MovilUpdateView(LoginRequiredMixin, UpdateView):
    model = Movil
    template_name = "productapp/editar_movil.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_lanzamiento']
    success_url = reverse_lazy('productos')
