from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.http import  HttpResponseNotFound


# importación de funcionalidad para creación de usuarios
from django.contrib.auth.forms import UserCreationForm

# importación de funcionalidad para login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

# importar custom decorators
from panel.decorators import authenticated_user, allowed_users

# Importación de modelos
from panel.models import Persona_Model, Servicio_Model, Proyecto_Model, Mensaje_Model, Buscar_FrontEnd_Model
from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Imagen_Model, Buscar_BackEnd_Model


# Importación de forms
from panel.forms import Persona_Form, Servicio_Form, Proyecto_Form, Mensaje_Form, Buscar_FrontEnd_Form
from panel.forms import Pagina_Form, Articulo_Form, Categoria_Form, Imagen_Form, Buscar_BackEnd_Form


#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

@login_required(login_url='entrar')
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
            'object_title' : 'Mensajes Contacto',
            'icon' : 'bi bi-messenger',
            'object_description' : 'Agregar o modificar mensajes del formulario de contacto',
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
            'icon' : 'bi bi-search',
            'object_description' : 'Agregar o modificar búsquedas de FrontEnd',
            'object_url' : 'panel:listar_busquedas_frontend',
        },
        {
            'object_title' : 'Búsquedas de BackEnd',
            'icon' : 'bi bi-search',
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


@login_required(login_url='entrar')
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
# Vistas para Login
#=======================================================================================================================================


@authenticated_user
def entrar(request, *args, **kwargs):
    '''Página de Login de la plataforma. '''
    # Sacar al usuario que ingresa a esta vista
    #logout(request)

    # Mensajes para el usuario
    status = ''

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # loguear al usuario con el usuario recién creado
                login(request, user)
                return redirect('panel:app_panel_index')
            else:
                base_url = reverse('panel:entrar')
                query_string =  urlencode({'status': 'ERROR'})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
                #return redirect('panel:entrar')
        else:
            base_url = reverse('panel:entrar')
            query_string =  urlencode({'status': 'ERROR'})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
            #return redirect('panel:entrar')

    if request.method == 'GET':
        status_get = request.GET.get('status')
        print(f'status_get: {status_get}')
        if status_get == 'ERROR':
            status = 'ERROR'

        status_get = request.GET.get('status')
        print(f'status_get: {status_get}')
        if status_get == 'SALIR':
            status = 'SALIR'

    form = AuthenticationForm()


    context = {
        'page': 'Acceso / Login',
        'status': status,
        'form': form,
    }


    return render(request, 'login/login.html', context)



# #@authenticated_user
# def entrar(request, *args, **kwargs):
#     '''Página de Login de la plataforma. '''

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         # autenticar al usuario
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # loguear al ususario con el usuario recién creado
#             login(request, user)
#             return redirect('panel:inicio')

#         else:
#             messages.info(request, 'Ocurrió un error: usuario o password incorrecto.')

#     context = {
#         'page': 'Entrar',

#     }

#     return render(request, 'login/login.html', context)



def salir(request, *args, **kwargs):
    logout(request)
    return redirect('panel:entrar')



# @login_required(login_url='entrar')
# def inicio(request, *args, **kwargs):
#     group = None
#     if request.user.groups.exists():
#         group = request.user.groups.all()[0].name
    
#     # Grupos de uusuarios
#     # admin
#     # gerente
#     # controlador
#     # supervisor
#     # guardia
#     # cliente
#     # Instalación


#     if group == 'admin':

#         clientes = Cliente.objects.all()
#         instalaciones = Instalacion.objects.all()
#         personas = Persona.objects.all()
    
#         total_clientes = clientes.count()
#         total_instalaciones = instalaciones.count()
#         total_personas = personas.count()
        

#         context = {
#             'page': 'Dashboard Admin',
#             'clientes' : clientes,
#             'instalaciones' : instalaciones,
#             'personas' : personas,

#             'total_clientes' : total_clientes,
#             'total_instalaciones' : total_instalaciones,
#             'total_personas' : total_personas,
#         }   
#         return render(request, 'login/dashboard_admin.html', context)



#     else:
#         return redirect('panel:salir')



#=======================================================================================================================================
# Vistas para Personas
#=======================================================================================================================================

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
def listar_mensajes(request, *args, **kwargs):
    '''Lista mensajes.'''
    
    object_list = Mensaje_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Mensajes Contacto',
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
    return render(request, 'panel/generic_list_mini.html', context)


@login_required(login_url='entrar')
def ver_mensaje(request, id, *args, **kwargs):
    '''Detalle de mensaje.'''
    
    itemObj = Mensaje_Model.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Mensajes Contacto',
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
    return render(request, 'panel/generic_detail_mini.html', context)


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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

    
@login_required(login_url='entrar')
def eliminar_mensaje(request, id, *args, **kwargs):
    '''Eliminar mensaje.'''
    
    itemObj = Mensaje_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_mensajes')

    context = {
        'page' : 'Eliminar Mensajes Contacto',
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

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
def listar_articulos(request, *args, **kwargs):
    '''Lista artículos.'''
    
    object_list = Articulo_Model.objects.all().order_by('date') # Lista de objetos
    
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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

    
@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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
    

@login_required(login_url='entrar')
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


@login_required(login_url='entrar')
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

@login_required(login_url='entrar')
def listar_busquedas_frontend(request, *args, **kwargs):
    '''Lista búsquedas.'''
    
    object_list = Buscar_FrontEnd_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Búsquedas de sitio web',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_frontend',
        'url_eliminar' : 'panel:eliminar_busqueda_frontend',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_search.html', context)


@login_required(login_url='entrar')
def listar_busquedas_backend(request, *args, **kwargs):
    '''Lista búsquedas.'''
    
    object_list = Buscar_BackEnd_Model.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Búsquedas de panel de administración',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_backend',
        'url_eliminar' : 'panel:eliminar_busqueda_backend',
        'object_list': object_list
    }
    return render(request, 'panel/generic_list_search.html', context)


@login_required(login_url='entrar')
def eliminar_busqueda_frontend(request, id, *args, **kwargs):
    '''Eliminar búsqueda.'''
    
    itemObj = Buscar_FrontEnd_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_busquedas_frontend')

    context = {
        'page' : 'Eliminar búsqueda de sitio web',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_frontend',
        'url_eliminar' : 'panel:eliminar_busqueda_frontend',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)


@login_required(login_url='entrar')
def eliminar_busqueda_backend(request, id, *args, **kwargs):
    '''Eliminar búsqueda.'''
    
    itemObj = Buscar_BackEnd_Model.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('panel:listar_busquedas_backend')

    context = {
        'page' : 'Eliminar búsqueda de panel de administración',
        'singular' : 'búsqueda',
        'plural' : 'búsquedas',
        'url_activo_index' : 'panel:listar_busquedas_backend',
        'url_eliminar' : 'panel:eliminar_busqueda_backend',
        'item': itemObj,
    }
    return render(request, 'panel/generic_delete_object.html', context)




# ===============================================================================================
# CREAR USUARIO
# ===============================================================================================


# @login_required(login_url='entrar')
# def crear_usuario(request, *args, **kwargs):    
#     # if request.user.is_authenticated:
#     #     return redirect('panel:inicio')
#     # else:
#     #     (revisar formulario enviado vía POST)


#     # Para llamar al formulario predeterminado de Django se usa esta línea
#     #form = UserCreationForm()

#     # Invocamos al formulario customizado con email
#     form = CustomUserCreationForm()

#     if request.method == 'POST':
#         # para guardar los datos con el formulario predeterminado de Django
#         #form = UserCreationForm(request.POST)

#         # para guardar datos con formulario customizado con email
#         form = CustomUserCreationForm(request.POST)
        
#         if form.is_valid():
#             # user = form.save(commit=False)
#             user = form.save()
#             username = form.clean_data.get('username')
#             messages.success(request, 'Cuenta creada correctamente.')

#             # esto es para asociar todos los nuevos usuarios al grupo 'cliente'
#             # group = Group.objects.get('cliente')
#             # user.groups.add(group)
#             # permite asociar un cliente a un usuario nuevo
#             # Cliente.objects.create(user=user,)

#             if user is not None:
#                 # loguear al ususario con el usuario recién creado
#                 login(request, user)
#                 return redirect('panel:inicio')

#     context = {
#         'page': 'Crear usuario',
#         'form' : form,
#         # 'clientes' : clientes,
#         # 'total_clientes' : total_clientes,
#         # 'total_pedidos' : total_pedidos,
#         # 'pendientes' : pendientes,
#         # 'entregados' : entregados,
#         # 'enviados' : enviados,
#         #'productos' : productos,
#     }

#     return render(request, 'login/crear_usuario.html', context)



# ===============================================================================================
# PERFIL
# ===============================================================================================

@login_required(login_url='entrar')
def modificar_perfil(request, *args, **kwargs):

    cliente = request.user.cliente
    form = Persona_Form(instance=cliente)
    # print(cliente)

    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    if group == 'cliente':
        # esto permite obtener el nombre del cliente asociado al usuario
        # cliente = request.user.cliente.nombre
        cliente = request.user.cliente


        if request.method == 'POST':
            form = Persona_Form(request.POST, request.FILES, instance=cliente)
            if form.is_valid():
                form.save()
                
                return redirect('panel:inicio')

        context = {
            'page': 'Ver perfil',
            'cliente' : cliente,
            'form' : form,
        }   

        return render(request, 'login/modificar_perfil_cliente.html', context)


@login_required(login_url='entrar')
def ver_perfil(request, id, *args, **kwargs):
    '''Sirve para revisar un elemento.'''
    itemObj = Persona_Model.objects.get(id=id)
    
    context = {
        'page' : 'Revisar perfil',
        'icon' : 'person',
        'color' : 'info',
        'color_table' : 'default',
        'description' : '',
        'singular' : 'persona',
        'plural' : 'personas',
        'url_activo_index' : 'persona_index',
        'url_inactivo_index' : 'persona_inactivo_index',
        'url_crear' : 'persona_crear',
        'url_ver' : 'persona_ver',
        'url_editar' : 'persona_editar',
        'url_desactivar' : 'persona_desactivar',
        'url_activar' : 'persona_activar',
        'url_eliminar' : 'persona_eliminar',
        #'asdf' : asdf,
        'item': itemObj
    }
    return render(request, 'login/ver_perfil_persona.html', context)


def handler404(request, exception):
    # return render(request, 'panel/404.html', status=404)
    return HttpResponseNotFound(render(request, 'panel/404.html'))