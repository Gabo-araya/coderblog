from django.urls import path
#from django.views.i18n import JavaScriptCatalog
import blog.views

#app_name = 'blog'
urlpatterns = [

#index
    path('', blog.views.app_blog_index, name='app_blog_index'),
    path('resultados_busqueda/', blog.views.resultados_busqueda, name='resultados_busqueda'),

    path('blog/', blog.views.listar_articulos, name='listar_articulos'),
    path('blog/<int:id>/', blog.views.ver_articulo, name='ver_articulo'),


    #JS-Catalog para mostrar widget admin para fechas y horas
    #path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),

]