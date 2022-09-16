from django.urls import path
from django.views.i18n import JavaScriptCatalog
import panel.views

app_name = 'panel'
urlpatterns = [

#index
    path('', panel.views.app_panel_index, name='app_panel_index'),

    
    # # login
    # path('', login.views.inicio, name='inicio'),
    # path('entrar/', login.views.entrar, name='entrar'),
    # path('salir/', login.views.salir, name='salir'),
    # path('crear_usuario/', login.views.crear_usuario, name='crear_usuario'),

    # path('ver_perfil/', login.views.ver_perfil, name='ver_perfil'),
    # path('modificar_perfil/', login.views.modificar_perfil, name='modificar_perfil'),

    # # Reset de password
    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),
    #     name='reset_password'),
    # path('reset_password_enviado/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_sent.html'), 
    #     name='password_reset_done'),
    # path('reset_password_confirmado/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_form.html'), 
    #     name='password_reset_confirm'),
    # path('reset_password_completado/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_done.html'), 
    #     name='password_reset_complete'),


#personas 
    path('listar_personas/', panel.views.listar_personas, name='listar_personas'),
    path('crear_persona/', panel.views.crear_persona, name='crear_persona'),
    path('ver_persona/<int:id>/', panel.views.ver_persona, name='ver_persona'),
    path('modificar_persona/<int:id>/', panel.views.modificar_persona, name='modificar_persona'),
    path('eliminar_persona/<int:id>/', panel.views.eliminar_persona, name='eliminar_persona'),

#servicio 
    path('listar_servicios/', panel.views.listar_servicios, name='listar_servicios'),
    path('crear_servicio/', panel.views.crear_servicio, name='crear_servicio'),
    path('ver_servicio/<int:id>/', panel.views.ver_servicio, name='ver_servicio'),
    path('modificar_servicio/<int:id>/', panel.views.modificar_servicio, name='modificar_servicio'),
    path('eliminar_servicio/<int:id>/', panel.views.eliminar_servicio, name='eliminar_servicio'),

#proyectos  
    path('listar_proyectos/', panel.views.listar_proyectos, name='listar_proyectos'),
    path('crear_proyecto/', panel.views.crear_proyecto, name='crear_proyecto'),
    path('ver_proyecto/<int:id>/', panel.views.ver_proyecto, name='ver_proyecto'),
    path('modificar_proyecto/<int:id>/', panel.views.modificar_proyecto, name='modificar_proyecto'),
    path('eliminar_proyecto/<int:id>/', panel.views.eliminar_proyecto, name='eliminar_proyecto'),
    
#mensajes  
    path('listar_mensajes/', panel.views.listar_mensajes, name='listar_mensajes'),
    path('ver_mensaje/<int:id>/', panel.views.ver_mensaje, name='ver_mensaje'),
    path('eliminar_mensaje/<int:id>/', panel.views.eliminar_mensaje, name='eliminar_mensaje'),

#paginas
    path('listar_paginas/', panel.views.listar_paginas, name='listar_paginas'),
    path('crear_pagina/', panel.views.crear_pagina, name='crear_pagina'),
    path('ver_pagina/<int:id>/', panel.views.ver_pagina, name='ver_pagina'),
    path('modificar_pagina/<int:id>/', panel.views.modificar_pagina, name='modificar_pagina'),
    path('eliminar_pagina/<int:id>/', panel.views.eliminar_pagina, name='eliminar_pagina'),

#articulos
    path('listar_articulos/', panel.views.listar_articulos, name='listar_articulos'),
    path('ver_articulo/<int:id>/', panel.views.ver_articulo, name='ver_articulo'),
    path('crear_articulo/', panel.views.crear_articulo, name='crear_articulo'),
    path('modificar_articulo/<int:id>/', panel.views.modificar_articulo, name='modificar_articulo'),
    path('eliminar_articulo/<int:id>/', panel.views.eliminar_articulo, name='eliminar_articulo'),

#categoria
    path('listar_categorias/', panel.views.listar_categorias, name='listar_categorias'),
    path('crear_categoria/', panel.views.crear_categoria, name='crear_categoria'),
    path('ver_categoria/<int:id>/', panel.views.ver_categoria, name='ver_categoria'),
    path('modificar_categoria/<int:id>/', panel.views.modificar_categoria, name='modificar_categoria'),
    path('eliminar_categoria/<int:id>/', panel.views.eliminar_categoria, name='eliminar_categoria'),

#imagenes
    path('listar_imagenes/', panel.views.listar_imagenes, name='listar_imagenes'),
    path('crear_imagen/', panel.views.crear_imagen, name='crear_imagen'),
    path('ver_imagen/<int:id>/', panel.views.ver_imagen, name='ver_imagen'),
    path('modificar_imagen/<int:id>/', panel.views.modificar_imagen, name='modificar_imagen'),
    path('eliminar_imagen/<int:id>/', panel.views.eliminar_imagen, name='eliminar_imagen'),

#buscar 
    path('resultados_busqueda/', panel.views.resultados_busqueda, name='resultados_busqueda'),
    path('listar_busquedas_frontend/', panel.views.listar_busquedas_frontend, name='listar_busquedas_frontend'),
    path('eliminar_busqueda_frontend/<int:id>/', panel.views.eliminar_busqueda_frontend, name='eliminar_busqueda_frontend'),
    path('listar_busquedas_backend/', panel.views.listar_busquedas_backend, name='listar_busquedas_backend'),
    path('eliminar_busqueda_backend/<int:id>/', panel.views.eliminar_busqueda_backend, name='eliminar_busqueda_backend'),

    #JS-Catalog para mostrar widget admin para fechas y horas
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),

]