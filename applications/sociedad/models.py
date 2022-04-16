from email.policy import default
from django.db import models
from django.conf import settings
from colorfield.fields import ColorField

# Create your models here.

class Sociedad(models.Model):
    """Model definition for Sociedad."""

    # TODO: Define fields here

    ESTADO_SUNAT = (
        (1, 'ACTIVO'),
        (2, 'BAJA'),
        )

    TIPO_DOCUMENTO = (
        ('6', 'RUC - REGISTRO ÚNICO DE CONTRIBUYENTE'),
        ('1', 'DNI - DOC. NACIONAL DE IDENTIDAD'),
        ('-', 'VARIOS - VENTAS MENORES A S/.700.00 Y OTROS'),
        ('4', 'CARNET DE EXTRANJERÍA'),
        ('7', 'PASAPORTE'),
        ('A', 'CÉDULA DIPLOMÁTICA DE IDENTIDAD'),
        ('0', 'NO DOMICILIADO, SIN RUC (EXPORTACIÓN)'),
        )

    tipo_documento = models.CharField('Tipo de Documento', choices=TIPO_DOCUMENTO, max_length=1)
    ruc = models.CharField('RUC', max_length=15)
    razon_social = models.CharField('Razón Social', max_length=100)
    nombre_comercial = models.CharField('Nombre Comercial', max_length=100)
    direccion_legal = models.CharField('Dirección Legal', max_length=100)
    ubigeo = models.CharField('Ubigeo', max_length=6)
    estado_sunat = models.IntegerField('Estado de Empresa según SUNAT', choices=ESTADO_SUNAT)
    logo = models.ImageField('Logo', upload_to='img/sociedad', height_field=None, width_field=None, max_length=None, blank=True, null=True, editable=False)
    color = ColorField(default='#FF0000', editable=False)
    created_at = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, blank=True, null=True, related_name='Sociedad_created_by', editable=False)
    updated_at = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False, blank=True, null=True, editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, blank=True, null=True, related_name='Sociedad_updated_by', editable=False)

    class Meta:
        """Meta definition for Sociedad."""

        verbose_name = 'Sociedad'
        verbose_name_plural = 'Sociedades'

    def __str__(self):
        """Unicode representation of Sociedad."""
        return self.razon_social

