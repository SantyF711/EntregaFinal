from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=150, blank=True)
    apellido = models.CharField(max_length=150, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    icono_perfil = models.ImageField(upload_to='iconos_perfil/', null=True, blank=True)

    def __str__(self):
        return self.username