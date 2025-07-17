from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.VistaLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
]