from django import forms
from .models import Receta, Post

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'preparacion', 'imagen']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 3}),
            'preparacion': forms.Textarea(attrs={'rows': 5}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['puntaje', 'comentario']
        widgets = {
            'puntaje': forms.Select(choices=[(i, f"{i} estrellas") for i in range(1, 6)]),
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }