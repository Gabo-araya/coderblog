from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from panel.models import Persona_Model, Servicio_Model, Proyecto_Model, Mensaje_Model, Buscar_FrontEnd_Model
from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Imagen_Model, Buscar_BackEnd_Model


#=======================================================================================================================================
# Forms 
#=======================================================================================================================================

class Mensaje_Form(ModelForm):
    class Meta:
        model = Mensaje_Model
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Mensaje_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            
            
            
class Buscar_FrontEnd_Form(ModelForm):
    class Meta:
        model = Buscar_FrontEnd_Model
        fields = [
            'name',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Buscar_BackEnd_Form, self).__init__(*args, **kwargs)
