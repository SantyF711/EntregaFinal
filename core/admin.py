from django.contrib import admin
from .models import Receta, Post 
from django.contrib.auth.admin import UserAdmin

admin.site.register(Receta)
admin.site.register(Post)