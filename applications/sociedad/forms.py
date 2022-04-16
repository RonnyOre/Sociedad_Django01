from django import forms
from .models import Sociedad

class SociedadForm(forms.ModelForm):
    class Meta:
        model = Sociedad
        fields=(
            'razon_social',
            'nombre_comercial',
            'direccion_legal',
            'ubigeo',
            'estado_sunat',
            )

    def __init__(self, *args, **kwargs):
        super(SociedadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True
