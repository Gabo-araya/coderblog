from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from django.db.models import Q

# Importación de modelos
from panel.models import Persona_Model, Servicio_Model, Proyecto_Model, Mensaje_Model, Buscar_FrontEnd_Model
from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Imagen_Model, Buscar_BackEnd_Model

# Importación de forms
from blog.forms import Mensaje_Form, Buscar_FrontEnd_Form


#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

def app_blog_index(request, *args, **kwargs):
    '''Lista de elementos con las que se pueden realizar acciones.'''
    
    personas_list = Persona_Model.objects.all()[:3] # Lista de personas
    servicios_list = Servicio_Model.objects.all()[:3] # Lista de servicios
    proyectos_list = Proyecto_Model.objects.all()[:3] # Lista de proyectos
    articulos_list = Articulo_Model.objects.filter(draft=False).order_by('date')[:3] # Lista de articulos
    paginas_list = Pagina_Model.objects.all() # Lista de paginas

    '''Crear mensaje.'''
    
    form = Mensaje_Form()
    error_message = ''
    success_message = ''
    if request.method == 'POST':
        form = Mensaje_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name = info['name']
            email = info['email']
            subject = info['subject']
            message = info['message']
            
            mensaje = Mensaje_Model(
                name = name, 
                email = email,
                subject = subject,
                message = message,
                )

            mensaje.save()
            #return redirect('app_blog_index')
            success_message = 'Envío exitoso'
            #mensaje exitoso
        
        else:
            #mensaje invalido
            print("form invalido")
            error_message = 'form invalido'
            
            
            
            

    # else: 
    #     #ningún mensaje
    #     error_message = ''
    #     success_message = ''


    context = {
        'page' : 'Inicio',
        'description' : 'Se pueden realizar acciones con los elementos listados a continuación.',
        'personas' : personas_list,
        'servicios' : servicios_list,
        'proyectos' : proyectos_list,
        'articulos' : articulos_list,
        'paginas' : paginas_list,
        'success_message' : success_message,
        'error_message' : error_message,
    }
    return render(request, 'blog/landing.html', context)
    







def resultados_busqueda(request, *args, **kwargs):
    '''Muestra resultados de búsqueda.'''
    
    form = Buscar_FrontEnd_Form()
    vacio = True
    termino_busqueda = ''
    result_articulo = ''
    
    if request.method == 'POST':
        form = Buscar_FrontEnd_Form(request.POST)
        if form.is_valid():
            #form.cleaned_data()
            termino_busqueda = form.cleaned_data['name']
            print(termino_busqueda)
            form.save()

        if termino_busqueda == '':
            vacio = True
        else:
            vacio = False
            result_articulo = Articulo_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(title__icontains=termino_busqueda) |
                Q(subtitle__icontains=termino_busqueda) |
                Q(abstract__icontains=termino_busqueda) |
                Q(content__icontains=termino_busqueda)
                ).filter(draft=False).order_by('date')

    paginas_list = Pagina_Model.objects.all() # Lista de paginas
    
    context = {
        'page': 'Resultados de búsqueda',
        'termino_busqueda': termino_busqueda,
        'vacio': vacio,
        # 'result_persona': result_persona,
        # 'result_servicio': result_servicio,
        # 'result_proyecto': result_proyecto,
        # 'result_pagina': result_pagina,
        'result_articulo': result_articulo,
        # 'result_categoria': result_categoria,
        # 'result_imagen': result_imagen,
        'paginas': paginas_list,
    }
    return render(request, 'blog/resultados_busqueda.html', context)



def listar_articulos(request, *args, **kwargs):
    '''Lista artículos.'''
    
    #object_list = Articulo_Model.objects.filter(draft=False) # Lista de objetos
    paginas_list = Pagina_Model.objects.all() # Lista de paginas
    articulos_list = Articulo_Model.objects.filter(draft=False).order_by('date') # Lista de articulos
    
    context = {
        'page' : 'Blog',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_ver' : 'ver_articulo',
        'paginas': paginas_list,
        'articulos': articulos_list,
    }
    return render(request, 'blog/lista.html', context)



def ver_articulo(request, id, *args, **kwargs):
    '''Detalle de artículo.'''
    
    itemObj = Articulo_Model.objects.filter(id=id) 
    #titulo = itemObj.title
    paginas_list = Pagina_Model.objects.all() # Lista de paginas
    articulos_list = Articulo_Model.objects.filter(draft=False) # Lista de articulos
    
    context = {
        #'page' : titulo,
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'listar_articulos',
        'paginas': paginas_list,
        'articulos': articulos_list,
        'item': list(itemObj),
    }
    return render(request, 'blog/detalle.html', context)


def crear_mensaje(request, *args, **kwargs):
    '''Crear mensaje.'''
    
    form = Mensaje_Form()
    
    if request.method == 'POST':
        form = Mensaje_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            name = info['name']
            email = info['email']
            subject = info['subject']
            message = info['message']
            
            mensaje = Mensaje_Model(
                name = name, 
                email = email,
                subject = subject,
                message = message,
                )

            mensaje.save()
            return redirect('app_blog_index')

    context = {
        'page' : 'Crear Mensaje',
        'icon' : 'bx bx-file',
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'panel:listar_mensajes',
        'url_crear' : 'panel:crear_mensaje',
        'url_ver' : 'panel:ver_mensaje',
        'url_editar' : 'panel:modificar_mensaje',
        'url_eliminar' : 'panel:eliminar_mensaje',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)

