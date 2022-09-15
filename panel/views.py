from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from django.db.models import Q

# Importación de modelos
from panel.models import Persona_Model, Servicio_Model, Proyecto_Model, Mensaje_Model, Buscar_FrontEnd_Model
from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Imagen_Model, Buscar_BackEnd_Model


# Importación de forms
from panel.forms import Persona_Form, Servicio_Form, Proyecto_Form, Mensaje_Form, Buscar_FrontEnd_Form
from panel.forms import Pagina_Form, Articulo_Form, Categoria_Form, Imagen_Form, Buscar_BackEnd_Form


#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

def app_panel_index(request, *args, **kwargs):
    '''Lista de elementos con las que se pueden realizar acciones.'''
    object_list = [
        {
            'object_title' : 'Personas',
            'icon' : 'bx bxs-user-rectangle',
            'object_description' : 'Agregar o modificar personas',
            'object_url' : 'panel:listar_personas',
        },
        {
            'object_title' : 'Servicios',
            'icon' : 'bx bxs-building-house',
            'object_description' : 'Agregar o modificar servicios',
            'object_url' : 'panel:listar_servicios',
        },
        {
            'object_title' : 'Proyectos',
            'icon' : 'bx bxs-user-pin',
            'object_description' : 'Agregar o modificar proyectos',
            'object_url' : 'panel:listar_proyectos',
        },
        {
            'object_title' : 'Mensajes',
            'icon' : 'bx bxs-user-pin',
            'object_description' : 'Agregar o modificar mensajes',
            'object_url' : 'panel:listar_mensajes',
        },
        {
            'object_title' : 'Páginas',
            'icon' : 'bx bxs-file',
            'object_description' : 'Agregar o modificar páginas',
            'object_url' : 'panel:listar_paginas',
        },
        {
            'object_title' : 'Artículos',
            'icon' : 'bx bx-file',
            'object_description' : 'Agregar o modificar articulos',
            'object_url' : 'panel:listar_articulos',
        },
        {
            'object_title' : 'Categorías',
            'icon' : 'bx bxs-extension',
            'object_description' : 'Agregar o modificar categorías',
            'object_url' : 'panel:listar_categorias',
        },
        {
            'object_title' : 'Imágenes',
            'icon' : 'bx bxs-image',
            'object_description' : 'Agregar o modificar imágenes',
            'object_url' : 'panel:listar_imagenes',
        },
        
        {
            'object_title' : 'Búsquedas de FrontEnd',
            'icon' : 'bx bxs-image',
            'object_description' : 'Agregar o modificar búsquedas de FrontEnd',
            'object_url' : 'panel:listar_busquedas_frontend',
        },
        {
            'object_title' : 'Búsquedas de BackEnd',
            'icon' : 'bx bxs-image',
            'object_description' : 'Agregar o modificar búsquedas de BackEnd',
            'object_url' : 'panel:listar_busquedas_backend',
        },
    ]

    context = {
        'page' : 'Inicio',
        'icon' : 'bi bi-grid',
        'description' : 'Se pueden realizar acciones con los elementos listados a continuación.',
        'object_list' : object_list,
    }
    return render(request, 'panel/app_index.html', context)


def resultados_busqueda(request, *args, **kwargs):
    '''Muestra resultados de búsqueda.'''
    form = Buscar_BackEnd_Form()
    vacio = True
    termino_busqueda = ''
    result_persona = ''
    result_servicio = ''
    result_proyecto = ''
    result_pagina = ''
    result_articulo = ''
    result_categoria = ''
    result_imagen = ''
    
    if request.method == 'POST':
        form = Buscar_BackEnd_Form(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['name']
            print(termino_busqueda)
            form.save()

        if termino_busqueda == '':
            vacio = True
        else:
            vacio = False
            result_persona = Persona_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(minibio__icontains=termino_busqueda) 
                )
            result_servicio = Servicio_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(description__icontains=termino_busqueda) 
                )
            result_proyecto = Proyecto_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(description__icontains=termino_busqueda) 
                )
            result_pagina = Pagina_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(title__icontains=termino_busqueda) |
                Q(subtitle__icontains=termino_busqueda) |
                Q(abstract__icontains=termino_busqueda) |
                Q(content__icontains=termino_busqueda)
                )
            result_articulo = Articulo_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(title__icontains=termino_busqueda) |
                Q(subtitle__icontains=termino_busqueda) |
                Q(abstract__icontains=termino_busqueda) |
                Q(content__icontains=termino_busqueda)
                )
            result_categoria = Categoria_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) |  
                Q(description__icontains=termino_busqueda) 
                )
            result_imagen = Imagen_Model.objects.distinct().filter(
                Q(name__icontains=termino_busqueda) 
                )

            # print('termino_busqueda: ', termino_busqueda)
            # print('result_persona: ', result_persona)
            # print('result_servicio: ', result_servicio)
            # print('result_proyecto: ', result_proyecto)
            # print('result_pagina: ', result_pagina)
            # print('result_articulo: ', result_articulo)
            # print('result_categoria: ', result_categoria)
            # print('result_imagen: ', result_imagen)

    context = {
        'page': 'Resultados de búsqueda',
        'icon': 'bi bi-grid',
        'termino_busqueda': termino_busqueda,
        'vacio': vacio,
        'result_persona': result_persona,
        'result_servicio': result_servicio,
        'result_proyecto': result_proyecto,
        'result_pagina': result_pagina,
        'result_articulo': result_articulo,
        'result_categoria': result_categoria,
        'result_imagen': result_imagen,
    }
    return render(request, 'panel/search_result.html', context)



#=======================================================================================================================================
# Vistas para Personas
#=======================================================================================================================================

def listar_personas(request, *args, **kwargs):
    '''Lista personas.'''
    
    object_list = Persona_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Personas',
        'icon' : 'bx bxs-building-house',
        'singular' : 'persona',
        'plural' : 'personas',
        'url_listar' : 'panel:listar_personas',
        'url_crear' : 'panel:crear_persona',
        'url_ver' : 'panel:ver_persona',
        'url_editar' : 'panel:modificar_persona',
        'url_eliminar' : 'panel:eliminar_persona',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_persona(request, id, *args, **kwargs):
    '''Detalle de persona.'''
    
    itemObj = Persona_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de persona',
        'icon' : 'bx bxs-building-house',
        'singular' : 'persona',
        'plural' : 'personas',
        'url_listar' : 'panel:listar_personas',
        'url_crear' : 'panel:crear_persona',
        'url_ver' : 'panel:ver_persona',
        'url_editar' : 'panel:modificar_persona',
        'url_eliminar' : 'panel:eliminar_persona',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_persona(request, *args, **kwargs):
    '''Crear persona.'''
    
    form = Persona_Form()
    
    if request.method == 'POST':
        form = Persona_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_personas')

    context = {
        'page' : 'Crear persona',
        'icon' : 'bx bxs-building-house',
        'singular' : 'persona',
        'plural' : 'personas',
        'url_listar' : 'panel:listar_personas',
        'url_crear' : 'panel:crear_persona',
        'url_ver' : 'panel:ver_persona',
        'url_editar' : 'panel:modificar_persona',
        'url_eliminar' : 'panel:eliminar_persona',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_persona(request, id, *args, **kwargs):
    '''Editar persona.'''
    
    itemObj = Persona_Model.objects.get(id=id) 
    form = Persona_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Persona_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_personas')

    context = {
        'page' : 'Editar persona',
        'icon' : 'bx bxs-building-house',
        'singular' : 'persona',
        'plural' : 'personas',
        'url_listar' : 'panel:listar_personas',
        'url_crear' : 'panel:crear_persona',
        'url_ver' : 'panel:ver_persona',
        'url_editar' : 'panel:modificar_persona',
        'url_eliminar' : 'panel:eliminar_persona',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_persona(request, id, *args, **kwargs):
    '''Eliminar persona.'''
    
    itemObj = Persona_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_personas')

    context = {
        'page' : 'Eliminar persona',
        'icon' : 'bx bxs-building-house',
        'singular' : 'persona',
        'plural' : 'personas',
        'url_listar' : 'panel:listar_personas',
        'url_crear' : 'panel:crear_persona',
        'url_ver' : 'panel:ver_persona',
        'url_editar' : 'panel:modificar_persona',
        'url_eliminar' : 'panel:eliminar_persona',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Servicios
#=======================================================================================================================================

def listar_servicios(request, *args, **kwargs):
    '''Lista servicios.'''
    
    object_list = Servicio_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Servicios',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'servicio',
        'plural' : 'servicios',
        'url_listar' : 'panel:listar_servicios',
        'url_crear' : 'panel:crear_servicio',
        'url_ver' : 'panel:ver_servicio',
        'url_editar' : 'panel:modificar_servicio',
        'url_eliminar' : 'panel:eliminar_servicio',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_servicio(request, id, *args, **kwargs):
    '''Detalle de servicio.'''
    
    itemObj = Servicio_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de servicio',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'servicio',
        'plural' : 'servicios',
        'url_listar' : 'panel:listar_servicios',
        'url_crear' : 'panel:crear_servicio',
        'url_ver' : 'panel:ver_servicio',
        'url_editar' : 'panel:modificar_servicio',
        'url_eliminar' : 'panel:eliminar_servicio',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_servicio(request, *args, **kwargs):
    '''Crear servicio.'''
    
    form = Servicio_Form()
    
    if request.method == 'POST':
        form = Servicio_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_servicios')

    context = {
        'page' : 'Crear servicio',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'servicio',
        'plural' : 'servicios',
        'url_listar' : 'panel:listar_servicios',
        'url_crear' : 'panel:crear_servicio',
        'url_ver' : 'panel:ver_servicio',
        'url_editar' : 'panel:modificar_servicio',
        'url_eliminar' : 'panel:eliminar_servicio',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_servicio(request, id, *args, **kwargs):
    '''Editar servicio.'''
    
    itemObj = Servicio_Model.objects.get(id=id) 
    form = Servicio_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Servicio_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_servicios')

    context = {
        'page' : 'Editar servicio',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'servicio',
        'plural' : 'servicios',
        'url_listar' : 'panel:listar_servicios',
        'url_crear' : 'panel:crear_servicio',
        'url_ver' : 'panel:ver_servicio',
        'url_editar' : 'panel:modificar_servicio',
        'url_eliminar' : 'panel:eliminar_servicio',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_servicio(request, id, *args, **kwargs):
    '''Eliminar servicio.'''
    
    itemObj = Servicio_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_servicios')

    context = {
        'page' : 'Eliminar servicio',
        'icon' : 'bx bxs-user-rectangle',
        'singular' : 'servicio',
        'plural' : 'servicios',
        'url_listar' : 'panel:listar_servicios',
        'url_crear' : 'panel:crear_servicio',
        'url_ver' : 'panel:ver_servicio',
        'url_editar' : 'panel:modificar_servicio',
        'url_eliminar' : 'panel:eliminar_servicio',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Proyectos
#=======================================================================================================================================


def listar_proyectos(request, *args, **kwargs):
    '''Lista proyectos.'''
    
    object_list = Proyecto_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Proyectos',
        'icon' : 'bx bxs-user-pin',
        'singular' : 'proyecto',
        'plural' : 'proyectos',
        'url_listar' : 'panel:listar_proyectos',
        'url_crear' : 'panel:crear_proyecto',
        'url_ver' : 'panel:ver_proyecto',
        'url_editar' : 'panel:modificar_proyecto',
        'url_eliminar' : 'panel:eliminar_proyecto',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_proyecto(request, id, *args, **kwargs):
    '''Detalle de proyecto.'''
    
    itemObj = Proyecto_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de proyecto',
        'icon' : 'bx bxs-user-pin',
        'singular' : 'proyecto',
        'plural' : 'proyectos',
        'url_listar' : 'panel:listar_proyectos',
        'url_crear' : 'panel:crear_proyecto',
        'url_ver' : 'panel:ver_proyecto',
        'url_editar' : 'panel:modificar_proyecto',
        'url_eliminar' : 'panel:eliminar_proyecto',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_proyecto(request, *args, **kwargs):
    '''Crear proyecto.'''
    
    form = Proyecto_Form()
    
    if request.method == 'POST':
        form = Proyecto_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_proyectos')

    context = {
        'page' : 'Crear proyecto',
        'icon' : 'bx bxs-user-pin',
        'singular' : 'proyecto',
        'plural' : 'proyectos',
        'url_listar' : 'panel:listar_proyectos',
        'url_crear' : 'panel:crear_proyecto',
        'url_ver' : 'panel:ver_proyecto',
        'url_editar' : 'panel:modificar_proyecto',
        'url_eliminar' : 'panel:eliminar_proyecto',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_proyecto(request, id, *args, **kwargs):
    '''Editar proyecto.'''
    
    itemObj = Proyecto_Model.objects.get(id=id) 
    form = Proyecto_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Proyecto_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_proyectos')

    context = {
        'page' : 'Editar proyecto',
        'icon' : 'bx bxs-user-pin',
        'singular' : 'proyecto',
        'plural' : 'proyectos',
        'url_listar' : 'panel:listar_proyectos',
        'url_crear' : 'panel:crear_proyecto',
        'url_ver' : 'panel:ver_proyecto',
        'url_editar' : 'panel:modificar_proyecto',
        'url_eliminar' : 'panel:eliminar_proyecto',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_proyecto(request, id, *args, **kwargs):
    '''Eliminar proyecto.'''
    
    itemObj = Proyecto_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_proyectos')

    context = {
        'page' : 'Eliminar proyecto',
        'icon' : 'bx bxs-user-pin',
        'singular' : 'proyecto',
        'plural' : 'proyectos',
        'url_listar' : 'panel:listar_proyectos',
        'url_crear' : 'panel:crear_proyecto',
        'url_ver' : 'panel:ver_proyecto',
        'url_editar' : 'panel:modificar_proyecto',
        'url_eliminar' : 'panel:eliminar_proyecto',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
    


#=======================================================================================================================================
# Vistas para Mensajes
#=======================================================================================================================================

def listar_mensajes(request, *args, **kwargs):
    '''Lista mensajes.'''
    
    object_list = Mensaje_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Mensajes',
        'icon' : 'bx bx-file',
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'panel:listar_mensajes',
        'url_crear' : 'panel:crear_mensaje',
        'url_ver' : 'panel:ver_mensaje',
        'url_editar' : 'panel:modificar_mensaje',
        'url_eliminar' : 'panel:eliminar_mensaje',
        'object_list': object_list
    }
    return render(request, 'panel/mensaje_list.html', context)


def ver_mensaje(request, id, *args, **kwargs):
    '''Detalle de mensaje.'''
    
    itemObj = Mensaje_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Mensaje',
        'icon' : 'bx bx-file',
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'panel:listar_mensajes',
        'url_crear' : 'panel:crear_mensaje',
        'url_ver' : 'panel:ver_mensaje',
        'url_editar' : 'panel:modificar_mensaje',
        'url_eliminar' : 'panel:eliminar_mensaje',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


# def crear_mensaje(request, *args, **kwargs):
#     '''Crear mensaje.'''
    
#     form = Mensaje_Form()
    
#     if request.method == 'POST':
#         form = Mensaje_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('panel:listar_mensajes')

#     context = {
#         'page' : 'Crear Mensaje',
#         'icon' : 'bx bx-file',
#         'singular' : 'mensaje',
#         'plural' : 'mensajes',
#         'url_listar' : 'panel:listar_mensajes',
#         'url_crear' : 'panel:crear_mensaje',
#         'url_ver' : 'panel:ver_mensaje',
#         'url_editar' : 'panel:modificar_mensaje',
#         'url_eliminar' : 'panel:eliminar_mensaje',
#         'form': form
#     }
#     return render(request, 'panel/generic_file_form.html', context)
    
    
# def modificar_mensaje(request, id, *args, **kwargs):
#     '''Editar mensaje.'''
    
#     itemObj = Mensaje_Model.objects.get(id=id) 
#     form = Mensaje_Form(instance=itemObj)
    
#     if request.method == 'POST':
#         form = Mensaje_Form(request.POST, request.FILES, instance=itemObj)
#         if form.is_valid():
#             form.save()
#             return redirect('panel:listar_mensajes')

#     context = {
#         'page' : 'Editar Mensaje',
#         'icon' : 'bx bx-file',
#         'singular' : 'mensaje',
#         'plural' : 'mensajes',
#         'url_listar' : 'panel:listar_mensajes',
#         'url_crear' : 'panel:crear_mensaje',
#         'url_ver' : 'panel:ver_mensaje',
#         'url_editar' : 'panel:modificar_mensaje',
#         'url_eliminar' : 'panel:eliminar_mensaje',
#         'item': itemObj,
#         'form': form,
#     }
#     return render(request, 'panel/generic_file_form.html', context)

    
    
def eliminar_mensaje(request, id, *args, **kwargs):
    '''Eliminar mensaje.'''
    
    itemObj = Mensaje_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_mensajes')

    context = {
        'page' : 'Eliminar Mensaje',
        'icon' : 'bx bx-file',
        'singular' : 'mensaje',
        'plural' : 'mensajes',
        'url_listar' : 'panel:listar_mensajes',
        'url_crear' : 'panel:crear_mensaje',
        'url_ver' : 'panel:ver_mensaje',
        'url_editar' : 'panel:modificar_mensaje',
        'url_eliminar' : 'panel:eliminar_mensaje',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
    


#=======================================================================================================================================
# Vistas para Páginas
#=======================================================================================================================================

def listar_paginas(request, *args, **kwargs):
    '''Lista páginas.'''
    
    object_list = Pagina_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Páginas',
        'icon' : 'bx bxs-file',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'panel:listar_paginas',
        'url_crear' : 'panel:crear_pagina',
        'url_ver' : 'panel:ver_pagina',
        'url_editar' : 'panel:modificar_pagina',
        'url_eliminar' : 'panel:eliminar_pagina',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_pagina(request, id, *args, **kwargs):
    '''Detalle de página.'''
    
    itemObj = Pagina_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de página',
        'icon' : 'bx bxs-file',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'panel:listar_paginas',
        'url_crear' : 'panel:crear_pagina',
        'url_ver' : 'panel:ver_pagina',
        'url_editar' : 'panel:modificar_pagina',
        'url_eliminar' : 'panel:eliminar_pagina',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_pagina(request, *args, **kwargs):
    '''Crear página.'''
    
    form = Pagina_Form()
    
    if request.method == 'POST':
        form = Pagina_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_paginas')

    context = {
        'page' : 'Crear página',
        'icon' : 'bx bxs-file',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'panel:listar_paginas',
        'url_crear' : 'panel:crear_pagina',
        'url_ver' : 'panel:ver_pagina',
        'url_editar' : 'panel:modificar_pagina',
        'url_eliminar' : 'panel:eliminar_pagina',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_pagina(request, id, *args, **kwargs):
    '''Editar página.'''
    
    itemObj = Pagina_Model.objects.get(id=id) 
    form = Pagina_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Pagina_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_paginas')

    context = {
        'page' : 'Editar página',
        'icon' : 'bx bxs-file',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'panel:listar_paginas',
        'url_crear' : 'panel:crear_pagina',
        'url_ver' : 'panel:ver_pagina',
        'url_editar' : 'panel:modificar_pagina',
        'url_eliminar' : 'panel:eliminar_pagina',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_pagina(request, id, *args, **kwargs):
    '''Eliminar página.'''
    
    itemObj = Pagina_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_paginas')

    context = {
        'page' : 'Eliminar página',
        'icon' : 'bx bxs-file',
        'singular' : 'página',
        'plural' : 'páginas',
        'url_listar' : 'panel:listar_paginas',
        'url_crear' : 'panel:crear_pagina',
        'url_ver' : 'panel:ver_pagina',
        'url_editar' : 'panel:modificar_pagina',
        'url_eliminar' : 'panel:eliminar_pagina',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Artículos
#=======================================================================================================================================

def listar_articulos(request, *args, **kwargs):
    '''Lista artículos.'''
    
    object_list = Articulo_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Artículos',
        'icon' : 'bx bx-file',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'panel:listar_articulos',
        'url_crear' : 'panel:crear_articulo',
        'url_ver' : 'panel:ver_articulo',
        'url_editar' : 'panel:modificar_articulo',
        'url_eliminar' : 'panel:eliminar_articulo',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_articulo(request, id, *args, **kwargs):
    '''Detalle de artículo.'''
    
    itemObj = Articulo_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Artículo',
        'icon' : 'bx bx-file',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'panel:listar_articulos',
        'url_crear' : 'panel:crear_articulo',
        'url_ver' : 'panel:ver_articulo',
        'url_editar' : 'panel:modificar_articulo',
        'url_eliminar' : 'panel:eliminar_articulo',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_articulo(request, *args, **kwargs):
    '''Crear artículo.'''
    
    form = Articulo_Form()
    
    if request.method == 'POST':
        form = Articulo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_articulos')

    context = {
        'page' : 'Crear Artículo',
        'icon' : 'bx bx-file',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'panel:listar_articulos',
        'url_crear' : 'panel:crear_articulo',
        'url_ver' : 'panel:ver_articulo',
        'url_editar' : 'panel:modificar_articulo',
        'url_eliminar' : 'panel:eliminar_articulo',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_articulo(request, id, *args, **kwargs):
    '''Editar artículo.'''
    
    itemObj = Articulo_Model.objects.get(id=id) 
    form = Articulo_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Articulo_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_articulos')

    context = {
        'page' : 'Editar Artículo',
        'icon' : 'bx bx-file',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'panel:listar_articulos',
        'url_crear' : 'panel:crear_articulo',
        'url_ver' : 'panel:ver_articulo',
        'url_editar' : 'panel:modificar_articulo',
        'url_eliminar' : 'panel:eliminar_articulo',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)

    
    
def eliminar_articulo(request, id, *args, **kwargs):
    '''Eliminar artículo.'''
    
    itemObj = Articulo_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_articulos')

    context = {
        'page' : 'Eliminar Artículo',
        'icon' : 'bx bx-file',
        'singular' : 'artículo',
        'plural' : 'artículos',
        'url_listar' : 'panel:listar_articulos',
        'url_crear' : 'panel:crear_articulo',
        'url_ver' : 'panel:ver_articulo',
        'url_editar' : 'panel:modificar_articulo',
        'url_eliminar' : 'panel:eliminar_articulo',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
    


#=======================================================================================================================================
# Vistas para Categorías
#=======================================================================================================================================

def listar_categorias(request, *args, **kwargs):
    '''Lista categorías.'''
    
    object_list = Categoria_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'categorías',
        'icon' : 'bx bxs-extension',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'panel:listar_categorias',
        'url_crear' : 'panel:crear_categoria',
        'url_ver' : 'panel:ver_categoria',
        'url_editar' : 'panel:modificar_categoria',
        'url_eliminar' : 'panel:eliminar_categoria',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_categoria(request, id, *args, **kwargs):
    '''Detalle de categoría.'''
    
    itemObj = Categoria_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de categoría',
        'icon' : 'bx bxs-extension',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'panel:listar_categorias',
        'url_crear' : 'panel:crear_categoria',
        'url_ver' : 'panel:ver_categoria',
        'url_editar' : 'panel:modificar_categoria',
        'url_eliminar' : 'panel:eliminar_categoria',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_categoria(request, *args, **kwargs):
    '''Crear categoría.'''
    
    form = Categoria_Form()
    
    if request.method == 'POST':
        form = Categoria_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_categorias')

    context = {
        'page' : 'Crear categoría',
        'icon' : 'bx bxs-extension',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'panel:listar_categorias',
        'url_crear' : 'panel:crear_categoria',
        'url_ver' : 'panel:ver_categoria',
        'url_editar' : 'panel:modificar_categoria',
        'url_eliminar' : 'panel:eliminar_categoria',
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)
    
    
def modificar_categoria(request, id, *args, **kwargs):
    '''Editar categoría.'''
    
    itemObj = Categoria_Model.objects.get(id=id) 
    form = Categoria_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Categoria_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_categorias')

    context = {
        'page' : 'Editar categoría',
        'icon' : 'bx bxs-extension',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'panel:listar_categorias',
        'url_crear' : 'panel:crear_categoria',
        'url_ver' : 'panel:ver_categoria',
        'url_editar' : 'panel:modificar_categoria',
        'url_eliminar' : 'panel:eliminar_categoria',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_form.html', context)


def eliminar_categoria(request, id, *args, **kwargs):
    '''Eliminar categoría.'''
    
    itemObj = Categoria_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_categorias')

    context = {
        'page' : 'Eliminar categoría',
        'icon' : 'bx bxs-extension',
        'singular' : 'categoría',
        'plural' : 'categorías',
        'url_listar' : 'panel:listar_categorias',
        'url_crear' : 'panel:crear_categoria',
        'url_ver' : 'panel:ver_categoria',
        'url_editar' : 'panel:modificar_categoria',
        'url_eliminar' : 'panel:eliminar_categoria',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Imágenes
#=======================================================================================================================================

def listar_imagenes(request, *args, **kwargs):
    '''Lista imágenes.'''
    
    object_list = Imagen_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Imágenes',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_activo_index' : 'panel:listar_imagenes',
        'url_crear' : 'panel:crear_imagen',
        'url_ver' : 'panel:ver_imagen',
        'url_editar' : 'panel:modificar_imagen',
        'url_eliminar' : 'panel:eliminar_imagen',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list.html', context)


def ver_imagen(request, id, *args, **kwargs):
    '''Detalle de imagen.'''
    
    itemObj = Imagen_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'panel:listar_imagenes',
        'url_crear' : 'panel:crear_imagen',
        'url_ver' : 'panel:ver_imagen',
        'url_editar' : 'panel:modificar_imagen',
        'url_eliminar' : 'panel:eliminar_imagen',
        'item': itemObj
    }
    return render(request, 'panel/generic_detail.html', context)


def crear_imagen(request, *args, **kwargs):
    '''Crear imagen.'''
    
    form = Imagen_Form()
    
    if request.method == 'POST':
        form = Imagen_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_imagenes')

    context = {
        'page' : 'Crear imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'panel:listar_imagenes',
        'url_crear' : 'panel:crear_imagen',
        'url_ver' : 'panel:ver_imagen',
        'url_editar' : 'panel:modificar_imagen',
        'url_eliminar' : 'panel:eliminar_imagen',
        'form': form
    }
    return render(request, 'panel/generic_file_form.html', context)
    
    
def modificar_imagen(request, id, *args, **kwargs):
    '''Editar imagen.'''
    
    itemObj = Imagen_Model.objects.get(id=id) 
    form = Imagen_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Imagen_Form(request.POST, request.FILES, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('panel:listar_imagenes')

    context = {
        'page' : 'Editar imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'panel:listar_imagenes',
        'url_crear' : 'panel:crear_imagen',
        'url_ver' : 'panel:ver_imagen',
        'url_editar' : 'panel:modificar_imagen',
        'url_eliminar' : 'panel:eliminar_imagen',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'panel/generic_file_form.html', context)


def eliminar_imagen(request, id, *args, **kwargs):
    '''Eliminar imagen.'''
    
    itemObj = Imagen_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_imagenes')

    context = {
        'page' : 'Eliminar imagen',
        'singular' : 'imagen',
        'plural' : 'imágenes',
        'url_listar' : 'panel:listar_imagenes',
        'url_crear' : 'panel:crear_imagen',
        'url_ver' : 'panel:ver_imagen',
        'url_editar' : 'panel:modificar_imagen',
        'url_eliminar' : 'panel:eliminar_imagen',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)



#=======================================================================================================================================
# Vistas para Búsquedas
#=======================================================================================================================================

def listar_busquedas_frontend(request, *args, **kwargs):
    '''Lista búsquedas.'''
    
    object_list = Buscar_FrontEnd_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Búsquedas',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_frontend',
        'url_eliminar' : 'panel:eliminar_busqueda_frontend',
        'object_list': object_list
    }
    return render(request, 'panel/listar_busquedas.html', context)


def listar_busquedas_backend(request, *args, **kwargs):
    '''Lista búsquedas.'''
    
    object_list = Buscar_BackEnd_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Búsquedas',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_backend',
        'url_eliminar' : 'panel:eliminar_busqueda_backend',
        'object_list': object_list
    }
    return render(request, 'panel/listar_busquedas.html', context)


def eliminar_busqueda_frontend(request, id, *args, **kwargs):
    '''Eliminar búsqueda.'''
    
    itemObj = Buscar_FrontEnd_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_busquedas_frontend')

    context = {
        'page' : 'Eliminar búsqueda',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_frontend',
        'url_eliminar' : 'panel:eliminar_busqueda_frontend',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)


def eliminar_busqueda_backend(request, id, *args, **kwargs):
    '''Eliminar búsqueda.'''
    
    itemObj = Buscar_BackEnd_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_busquedas_backend')

    context = {
        'page' : 'Eliminar búsqueda',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_backend',
        'url_eliminar' : 'panel:eliminar_busqueda_backend',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)
