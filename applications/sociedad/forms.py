from django import forms
from .models import Documento, Sociedad, RepresentanteLegal

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

class EstadoSunatForm(forms.ModelForm):
    class Meta:
        model = Sociedad
        fields=(
            'estado_sunat',
            )

    def __init__(self, *args, **kwargs):
        super(EstadoSunatForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True
            visible.field.disabled = True

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = (
            'nombre_documento',
            'descripcion_documento',
            'documento',
            )

    def __init__(self, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True

class RepresentanteLegalForm(forms.ModelForm):
    class Meta:
        model = RepresentanteLegal
        fields = (
            'usuario',
            'tipo_representante_legal',
            'fecha_registro',
            )

        widgets = {
            'fecha_registro' : forms.DateInput(
                attrs ={
                    'type':'date',
                    },
                format = '%Y-%m-%d',
                ), 
        }

    def __init__(self, *args, **kwargs):
        super(RepresentanteLegalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True

class EstadoForm(forms.ModelForm):
    class Meta:
        model = RepresentanteLegal
        fields = (
            'fecha_baja',
            'estado',
            )

        widgets = {
            'fecha_baja' : forms.DateInput(
                attrs ={
                    'type':'date',
                    },
                format = '%Y-%m-%d',
                ), 
        }

    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True
        self.fields['estado'].disabled = True


