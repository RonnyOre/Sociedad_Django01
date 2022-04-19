from django.urls import path
from . import views

app_name='sociedad_app'

urlpatterns = [
    path('sociedad/', views.SociedadListView.as_view(), name='sociedad_inicio'),
    path('sociedad/actualizar/<pk>/', views.SociedadUpdateView.as_view(), name='sociedad_actualizar'),
    path('sociedad/baja/<pk>/', views.EstadoBajaUpdateView.as_view(), name='sociedad_baja'),
    path('sociedad/alta/<pk>/', views.EstadoAltaUpdateView.as_view(), name='sociedad_alta'),
    path('sociedad/detalle/<pk>/', views.SociedadDetailView.as_view(), name='sociedad_detalle'),
    path('documento/registrar/<int:sociedad_id>/', views.DocumentoCreateView.as_view(), name='documento_registrar'),
    path('documento/eliminar/<pk>/', views.DocumentoDeleteView.as_view(), name='documento_eliminar'),    
    path('representante/registrar/<int:sociedad_id>/', views.RepresentanteCreateView.as_view(), name='representante_registrar'),
    path('representante/baja/<pk>/', views.RepresentanteUpdateView.as_view(), name='representante_baja'),
]