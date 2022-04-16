from django.contrib import admin

from applications.sociedad.models import Sociedad

# Register your models here.

class SociedadAdmin(admin.ModelAdmin):
    '''Admin View for Sociedad'''

    list_display = (
        'razon_social',
        'ruc',
        'direccion_legal',
        'ubigeo',
        'estado_sunat',
        )

    ordering = (
        'razon_social',
        )
    
    def save_model(self, request, obj, form, change):
        if obj.created_by == None:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Sociedad, SociedadAdmin)