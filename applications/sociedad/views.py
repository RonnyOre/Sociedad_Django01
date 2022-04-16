from django.shortcuts import render
from django.urls.base import reverse_lazy
from .forms import SociedadForm
from .models import Sociedad
from django.views.generic import (
    ListView,
    UpdateView,
)

# Create your views here.

class SociedadListView(ListView):
    model = Sociedad
    template_name = "sociedad/sociedad/inicio.html"
    context_object_name = 'sociedades'

class SociedadUpdateView(UpdateView):
    model = Sociedad
    template_name = "sociedad/sociedad/update.html"
    form_class = SociedadForm
    success_url = reverse_lazy('sociedad_app:sociedad_inicio')

    def get_context_data(self, **kwargs):
        context = super(SociedadUpdateView, self).get_context_data(**kwargs)
        context['accion']="Actualizar"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_inicio')
        return context