from django.contrib import admin
from .models import Familiar, Amigo, Trabajo, Blog

# ====================
# Registro de Modelos en el Panel de Administración
# ====================

# Registro del modelo Familiar
@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'fecha_nacimiento')
    search_fields = ('nombre',)
    list_filter = ('edad',)
    ordering = ('nombre',)

# Registro del modelo Amigo
@admin.register(Amigo)
class AmigoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'familiar')
    search_fields = ('nombre', 'telefono', 'email')
    list_filter = ('familiar',)
    ordering = ('nombre',)

# Registro del modelo Trabajo
@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'posicion', 'salario')
    search_fields = ('nombre_empresa', 'posicion')
    list_filter = ('nombre_empresa', 'posicion')
    ordering = ('nombre_empresa',)

# Registro del modelo Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('fecha', 'autor')
    ordering = ('-fecha',)

