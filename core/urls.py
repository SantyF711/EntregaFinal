from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('recetas/', views.ver_recetas, name='ver_recetas'),
    path('mis-recetas/', views.mis_recetas, name='mis_recetas'),
    path('crear-receta/', views.crear_receta, name='crear_receta'),
    path('recetas/<int:pk>/editar/', views.editar_receta, name='editar_receta'),
    path('recetas/<int:pk>/borrar/', views.borrar_receta, name='borrar_receta'),
    path('recetas/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('recetas/buscar/', views.recetas_buscar, name='recetas_buscar'),
    path('comentario/eliminar/<int:post_id>/', views.eliminar_comentario, name='eliminar_comentario'),
]