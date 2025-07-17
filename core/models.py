from django.db import models
from django.conf import settings

class Receta(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recetas'
    )
    titulo = models.CharField(max_length=255)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='recetas_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Post(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='posts')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    puntaje = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.receta.titulo} - {self.puntaje} estrellas"