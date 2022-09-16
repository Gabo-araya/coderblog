# Generated by Django 3.2 on 2022-09-16 15:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_auto_20220915_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buscar_backend_model',
            options={'ordering': ['id'], 'verbose_name': 'Búsqueda Backend', 'verbose_name_plural': 'Búsquedas Backend'},
        ),
        migrations.AlterModelOptions(
            name='buscar_frontend_model',
            options={'ordering': ['id'], 'verbose_name': 'Búsqueda Frontend', 'verbose_name_plural': 'Búsquedas Frontend'},
        ),
        migrations.AlterModelOptions(
            name='proyecto_model',
            options={'ordering': ['id'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterField(
            model_name='articulo_model',
            name='abstract',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='articulo_model',
            name='content',
            field=ckeditor.fields.RichTextField(default='text', verbose_name='Contenido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria_model',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='pagina_model',
            name='abstract',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='pagina_model',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='persona_model',
            name='minibio',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Mini Biografía'),
        ),
        migrations.AlterField(
            model_name='proyecto_model',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='servicio_model',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]