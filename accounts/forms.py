from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class FormularioRegistro(UserCreationForm):
    nombre = forms.CharField(required=False, label="Nombre (opcional)")
    apellido = forms.CharField(required=False, label="Apellido (opcional)")
    fecha_nacimiento = forms.DateField(required=False, label="Fecha de nacimiento (opcional)",
                                       widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True, label="Correo electrónico")
    icono_perfil = forms.ImageField(label="Icono de perfil", required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'icono_perfil', 'nombre', 'apellido', 'fecha_nacimiento', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombre', 'apellido', 'fecha_nacimiento', 'icono_perfil']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'icono_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }