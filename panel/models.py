from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
import calendar, datetime

from ckeditor.fields import RichTextField

#=======================================================================================================================================
# Modelos:
    # Persona
    # Servicio
    # Proyecto
    # Buscar_FrontEnd
    # Pagina
    # Articulo
    # Categoria
    # Imagen
    # Buscar_BackEnd
#=======================================================================================================================================


#=======================================================================================================================================
# Modelos para FrontEnd
#=======================================================================================================================================


class Persona_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    phone = models.CharField(max_length=250, null=True, blank=True, verbose_name='Teléfono')
    # minibio = models.TextField(null=True, blank=True, verbose_name='Mini Biografía')
    minibio = RichTextField(null=True, blank=True, verbose_name='Mini Biografía')
    image = models.ImageField(null=True, blank=True, upload_to='img_persona/', default='', verbose_name='Imagen')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Autor') 

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']

    def __str__(self):
        return self.name



class Servicio_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    # description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    description = RichTextField(null=True, blank=True, verbose_name='Descripción')
    image = models.ImageField(null=True, blank=True, upload_to='img_servicio/', default='', verbose_name='Imagen')
    fk_categoria = models.ForeignKey('Categoria_Model', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoría') 

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['id']

    def __str__(self):
        return self.name



class Proyecto_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    # description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    description = RichTextField(null=True, blank=True, verbose_name='Descripción')
    image = models.ImageField(null=True, blank=True, upload_to='img_proyecto/', default='', verbose_name='Imagen')
    fk_categoria = models.ForeignKey('Categoria_Model', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoría') 

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']

    def __str__(self):
        return self.name



class Mensaje_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.EmailField(max_length=250, verbose_name='Email')
    subject = models.CharField(max_length=250, verbose_name='Asunto')
    message = models.TextField(verbose_name='Mensaje')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['id']

    def __str__(self):
        return self.subject
    
    

class Buscar_FrontEnd_Model(models.Model):
    ''' Guarda las búsquedas del FrontEnd. '''
    name = models.CharField(max_length=250, verbose_name='Término de búsqueda')
    created  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
        
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Búsqueda Frontend'
        verbose_name_plural = 'Búsquedas Frontend'
        ordering = ['id']

    def __str__(self):
        return self.name



#=======================================================================================================================================
# Modelos para blog
#=======================================================================================================================================

class Pagina_Model(models.Model):
    name = models.CharField(max_length=250, default='Sin nombre', verbose_name='Nombre')
    title = models.CharField(max_length=250, default='Sin título', verbose_name='Título')
    subtitle = models.CharField(max_length=250, null=True, blank=True, verbose_name='Subtítulo')
    # abstract = models.TextField(null=True, blank=True, verbose_name='Resumen')
    abstract = RichTextField(null=True, blank=True, verbose_name='Resumen')
    # content = models.TextField(null=True, blank=True, verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha')

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de última modificación')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['id']

    def __str__(self):
        return self.name



class Articulo_Model(models.Model):
    name = models.CharField(max_length=250, default='Sin nombre', verbose_name='Nombre')
    title = models.CharField(max_length=250, default='Sin título', verbose_name='Título')
    subtitle = models.CharField(max_length=250, null=True, blank=True, verbose_name='Subtítulo')
    # abstract = models.TextField(null=True, blank=True, verbose_name='Resumen')
    abstract = RichTextField(null=True, blank=True, verbose_name='Resumen')
    # content = models.TextField(null=True, blank=True, verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(null=True, blank=True, upload_to='img_articulo/', default='', verbose_name='Imagen')
    date = models.DateField(null=True, blank=True, verbose_name='Fecha')
    draft = models.BooleanField(null=True, blank=True, default=True, verbose_name='Borrador')
    fk_categoria = models.ForeignKey('Categoria_Model', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoría') 
    #fk_autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Autor') 

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de última modificación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']

    def __str__(self):
        return self.name



class Categoria_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    # description = models.TextField(null=True, blank=True, default='', verbose_name='Descripción')
    description = RichTextField(null=True, blank=True, verbose_name='Descripción')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

    def __str__(self):
        return self.name



class Imagen_Model(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    image = models.ImageField(null=True, blank=True, upload_to='imagenes/', default='', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de publicación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        ordering = ['id']

    def __str__(self):
        return self.name



#=======================================================================================================================================
# Modelos para BackEnd
#=======================================================================================================================================

class Buscar_BackEnd_Model(models.Model):
    ''' Guarda las búsquedas del BackEnd. '''
    name = models.CharField(max_length=250, verbose_name='Término de búsqueda')
    created  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Búsqueda Backend'
        verbose_name_plural = 'Búsquedas Backend'
        ordering = ['id']

    def __str__(self):
        return self.name


