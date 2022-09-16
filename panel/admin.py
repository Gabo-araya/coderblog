from django.contrib import admin

# Importación de modelos
from panel.models import Persona_Model, Servicio_Model, Proyecto_Model, Mensaje_Model, Buscar_FrontEnd_Model
from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Imagen_Model, Buscar_BackEnd_Model


admin.site.register(Persona_Model)
admin.site.register(Servicio_Model)
admin.site.register(Proyecto_Model)
admin.site.register(Mensaje_Model)
admin.site.register(Buscar_FrontEnd_Model)
admin.site.register(Pagina_Model)
admin.site.register(Articulo_Model)
admin.site.register(Categoria_Model)
admin.site.register(Imagen_Model)
admin.site.register(Buscar_BackEnd_Model)
