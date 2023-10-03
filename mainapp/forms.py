from django import forms
  
class PostFormulario(forms.Form):
    post = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=500)
    texto = forms.CharField(widget=forms.Textarea)
    
    
class BusquedaFormulario(forms.Form):
    post = forms.CharField(max_length=50, required=False)
    