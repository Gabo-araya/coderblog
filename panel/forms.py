from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from panel.models import Persona_Model, Servicio_Model, Proyecto_Model, Mensaje_Model, Buscar_FrontEnd_Model
from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Imagen_Model, Buscar_BackEnd_Model


#=======================================================================================================================================
# Forms 
#=======================================================================================================================================

class Persona_Form(ModelForm):
    class Meta:
        model = Persona_Model
        fields = [
            'name',
            'phone',
            'minibio',
            'image',
            'usuario',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['phone'].widget.attrs.update({'class':'form-control'})
        self.fields['minibio'].widget.attrs.update({'class':'form-control'})
        self.fields['image'].widget.attrs.update({'class':'form-control-file'})
        self.fields['usuario'].widget.attrs.update({'class':'form-control'})
        
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})
        
        
        
class Servicio_Form(ModelForm):
    class Meta:
        model = Servicio_Model
        fields = [
            'name',
            'description',
            'image',
            'fk_categoria',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Servicio_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['image'].widget.attrs.update({'class':'form-control-file'})
        self.fields['fk_categoria'].widget.attrs.update({'class':'form-control'})

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})
        
        
        
class Proyecto_Form(ModelForm):
    class Meta:
        model = Proyecto_Model
        fields = [
            'name',
            'description',
            'image',
            'fk_categoria',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Proyecto_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['image'].widget.attrs.update({'class':'form-control-file'})
        self.fields['fk_categoria'].widget.attrs.update({'class':'form-control'})
        
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})

        
        
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
    #     super(Buscar_FrontEnd_Form, self).__init__(*args, **kwargs)



class Pagina_Form(ModelForm):
    date = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = Pagina_Model
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            'content',
            'date',
        ]

        # widgets = {
        #     'name': forms.TextInput(attrs={"class": "form-control",}),
        #     'title': forms.TextInput(attrs={"class": "form-control",}),
        #     'subtitle': forms.TextInput(attrs={"class": "form-control",}),
        # }
    def __init__(self, *args, **kwargs):
        super(Pagina_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['subtitle'].widget.attrs.update({'class':'form-control'})
        self.fields['abstract'].widget.attrs.update({'class':'form-control'})
        self.fields['content'].widget.attrs.update({'class':'form-control'})
        #date



class Articulo_Form(ModelForm):
    date = forms.DateField(widget=AdminDateWidget())
        
    class Meta:
        model = Articulo_Model
        fields = [
            'name',
            'title',
            'subtitle',
            'abstract',
            'content',
            'image',
            'draft',
            'fk_categoria',
            'date',
        ]

    def __init__(self, *args, **kwargs):
        super(Articulo_Form, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['subtitle'].widget.attrs.update({'class':'form-control'})
        self.fields['abstract'].widget.attrs.update({'class':'form-control'})
        self.fields['content'].widget.attrs.update({'class':'form-control'})
        self.fields['image'].widget.attrs.update({'class':'form-control-file'})
        self.fields['draft'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_categoria'].widget.attrs.update({'class':'form-control'})
        #date



class Categoria_Form(ModelForm):
    class Meta:
        model = Categoria_Model
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(Categoria_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class Imagen_Form(ModelForm):
    class Meta:
        model = Imagen_Model
        fields = [
            'name',
            'image',
        ]
    def __init__(self, *args, **kwargs):
        super(Imagen_Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['image'].widget.attrs.update({'class':'form-control-file'})



class Buscar_BackEnd_Form(ModelForm):
    class Meta:
        model = Buscar_BackEnd_Model
        fields = [
            'name',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Buscar_BackEnd_Form, self).__init__(*args, **kwargs)
