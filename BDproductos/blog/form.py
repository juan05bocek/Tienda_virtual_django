from django import forms
from .models import Post

class Formulariopost(forms.ModelForm):
    class Meta: 
        model= Post
        fields = ('categoria', 'titulo', 'contenido', 'imagen')