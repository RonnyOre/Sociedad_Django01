from datetime import date
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .forms import SociedadForm, EstadoSunatForm, DocumentoForm, RepresentanteLegalForm, EstadoForm
from .models import  Sociedad, Documento, RepresentanteLegal
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)

# Create your views here.

class SociedadListView(ListView):
    model = Sociedad
    template_name = "sociedad/sociedad/inicio.html"
    context_object_name = 'sociedades'

class SociedadUpdateView(UpdateView):
    model = Sociedad
    template_name = "sociedad/sociedad/actualizar.html"
    form_class = SociedadForm
    success_url = reverse_lazy('sociedad_app:sociedad_inicio')

    def get_context_data(self, **kwargs):
        context = super(SociedadUpdateView, self).get_context_data(**kwargs)
        context['accion']="Actualizar"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_inicio')
        return context

class EstadoBajaUpdateView(UpdateView):
    model = Sociedad
    template_name = "sociedad/sociedad/estado.html"
    form_class = EstadoSunatForm
    success_url = reverse_lazy('sociedad_app:sociedad_inicio')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.estado_sunat = 2
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EstadoBajaUpdateView, self).get_context_data(**kwargs)
        context['accion']="Dar Baja"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_inicio')
        return context

class EstadoAltaUpdateView(UpdateView):
    model = Sociedad
    template_name = "sociedad/sociedad/estado.html"
    form_class = EstadoSunatForm
    success_url = reverse_lazy('sociedad_app:sociedad_inicio')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.estado_sunat = 1
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EstadoAltaUpdateView, self).get_context_data(**kwargs)
        context['accion']="Dar Alta"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_inicio')
        return context

class SociedadDetailView(DetailView):
    model = Sociedad
    template_name = "sociedad/sociedad/detalle.html"
    context_object_name = 'sociedad'

    def get_context_data(self, **kwargs):
        sociedad = Sociedad.objects.get(id = self.kwargs['pk'])
        context = super(SociedadDetailView, self).get_context_data(**kwargs)
        context['documentos'] = Documento.objects.filter(sociedad = sociedad)
        context['representantes'] = RepresentanteLegal.objects.filter(sociedad = sociedad)
        return context
    
class DocumentoCreateView(CreateView):
    model = Documento
    template_name = "sociedad/documento/registrar.html"
    form_class = DocumentoForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.kwargs['sociedad_id']})

    def form_valid(self, form):
        form.instance.sociedad = Sociedad.objects.get(id = self.kwargs['sociedad_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DocumentoCreateView, self).get_context_data(**kwargs)
        context['accion']="Registrar"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.kwargs['sociedad_id']})
        return context

class DocumentoDeleteView(DeleteView):
    model = Documento
    template_name = "sociedad/documento/eliminar.html"
    context_object_name = 'documentos' 

    def get_success_url(self, **kwargs):
        return reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.object.sociedad.id})

    def get_context_data(self, **kwargs):
        context = super(DocumentoDeleteView, self).get_context_data(**kwargs)
        context['accion']="Eliminar"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.object.sociedad.id})
        return context

class RepresentanteCreateView(CreateView):
    model = RepresentanteLegal
    template_name = "sociedad/representante/registrar.html"
    form_class = RepresentanteLegalForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.kwargs['sociedad_id']})

    def form_valid(self, form):
        form.instance.sociedad = Sociedad.objects.get(id = self.kwargs['sociedad_id'])
        obj = form.save(commit=False)

        if obj.fecha_registro > date.today():
            form.add_error('fecha_registro', 'La fecha de registro no puede ser mayor a la fecha de hoy.')
            return super(RepresentanteCreateView, self).form_invalid(form)

        obj.estado = 1
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RepresentanteCreateView, self).get_context_data(**kwargs)
        context['accion']="Registrar"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.kwargs['sociedad_id']})
        return context

class RepresentanteUpdateView(UpdateView):
    model = RepresentanteLegal
    template_name = "sociedad/representante/estado.html"
    form_class = EstadoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.object.sociedad.id})

    def form_valid(self, form):
        obj = form.save(commit=False)

        if obj.fecha_baja < obj.fecha_registro:
            form.add_error('fecha_baja', 'La fecha de baja no puede ser menor a la fecha de registro.')
            return super(RepresentanteUpdateView, self).form_invalid(form)   

        obj.estado = 2
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RepresentanteUpdateView, self).get_context_data(**kwargs)
        context['accion']="Dar Baja"
        context['previous'] = reverse_lazy('sociedad_app:sociedad_detalle', kwargs={'pk':self.object.sociedad.id})
        return context