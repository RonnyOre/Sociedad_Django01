# Generated by Django 3.2.12 on 2022-04-19 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sociedad', '0008_rename_descripcion_docuemnto_documento_descripcion_documento'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRepresentanteLegal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Modificación')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoRepresentanteLegal_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoRepresentanteLegal_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo Representante Legal',
                'verbose_name_plural': 'Tipos Representante Legal',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='RepresentanteLegal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(blank=True, null=True, verbose_name='Fecha de Registro')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Modificación')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='RepresentanteLegal_created_by', to=settings.AUTH_USER_MODEL)),
                ('sociedad', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Sociedad', to='sociedad.sociedad')),
                ('tipo_representante_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoRepresentanteLegal', to='sociedad.tiporepresentantelegal')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='RepresentanteLegal_updated_by', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Representante Legal',
                'verbose_name_plural': 'Representantes Legales',
            },
        ),
    ]
