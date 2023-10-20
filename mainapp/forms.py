from django import forms
from ckeditor.fields import RichTextFormField

class PostFormularioBase(forms.Form):
    post = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=500)
    texto = RichTextFormField()


class CrearPostFormulario(PostFormularioBase):
    ...
     
class EditarPostFormulario(PostFormularioBase):
    ...
    
class PostBusquedaFormulario(forms.Form):
    post = forms.CharField(max_length=50, required=False)