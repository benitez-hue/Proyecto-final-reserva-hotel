from django.contrib import admin
from django.urls import path, include
from familiares import views as familiares_views

# ====================
# DEFINICIÓN DE RUTAS (URLS)
# ====================
urlpatterns = [
    # Página principal
    path('', familiares_views.index, name='index'),

    # Panel de administración
    path('admin/', admin.site.urls),

    # Rutas de la app 'familiares' (CRUD de familiares, amigos, trabajos y blogs)
    path('familiares/', include('familiares.urls')),

    # Rutas de autenticación (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta para el registro de usuario (signup)
    path('accounts/signup/', familiares_views.signup, name='signup'),
]
