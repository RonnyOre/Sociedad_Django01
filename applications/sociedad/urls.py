from django.urls import path
from . import views

app_name='sociedad_app'

urlpatterns = [
    path('sociedad/', views.SociedadListView.as_view(), name='sociedad_inicio'),
    path('sociedad/actualizar/<pk>/', views.SociedadUpdateView.as_view(), name='sociedad_actualizar'),
]