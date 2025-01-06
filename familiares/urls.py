from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Rutas CRUD para Familiares
    path('familiares/', views.lista_familiares, name='lista_familiares'),
    path('familiares/agregar/', views.agregar_familiar, name='agregar_familiar'),
    path('familiares/editar/<int:pk>/', views.editar_familiar, name='editar_familiar'),
    path('familiares/eliminar/<int:pk>/', views.eliminar_familiar, name='eliminar_familiar'),

    # Rutas CRUD para Amigos
    path('amigos/', views.lista_amigos, name='lista_amigos'),
    path('amigos/agregar/', views.agregar_amigo, name='agregar_amigo'),
    path('amigos/editar/<int:pk>/', views.editar_amigo, name='editar_amigo'),

    # Rutas CRUD para Trabajos
    path('trabajos/', views.lista_trabajos, name='lista_trabajos'),
    path('trabajos/agregar/', views.agregar_trabajo, name='agregar_trabajo'),

    # Rutas CRUD para Blogs
    path('blogs/', views.lista_blogs, name='lista_blogs'),
    path('blogs/detalle/<int:pk>/', views.detalle_blog, name='detalle_blog'),
]
