import os
import django
import random
from datetime import date
from django.contrib.auth.models import User
from familiares.models import Familiar, Amigo, Trabajo, Blog

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tercera_entrega.settings')
django.setup()

# ====================
# Datos Aleatorios
# ====================

# Crear usuarios de prueba
usernames = ['usuario1', 'usuario2', 'usuario3']
for username in usernames:
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password='1234')

# Crear familiares
familiares_nombres = ['Ana', 'Luis', 'María', 'Carlos', 'Laura']
for nombre in familiares_nombres:
    Familiar.objects.get_or_create(
        nombre=nombre,
        edad=random.randint(20, 80),
        fecha_nacimiento=date(random.randint(1940, 2005), random.randint(1, 12), random.randint(1, 28))
    )

# Crear amigos
amigos_nombres = ['Pedro', 'Marta', 'Jorge', 'Sofía', 'Miguel']
for nombre in amigos_nombres:
    Amigo.objects.get_or_create(
        nombre=nombre,
        telefono=f'+549{random.randint(1000000000, 9999999999)}',
        email=f'{nombre.lower()}@example.com'
    )

# Crear trabajos
trabajos = [
    {'nombre_empresa': 'Hotel Sol', 'posicion': 'Recepcionista', 'salario': 120000, 'descripcion': 'Atención al cliente en recepción.'},
    {'nombre_empresa': 'Hotel Luna', 'posicion': 'Cocinero', 'salario': 150000, 'descripcion': 'Encargado de la cocina principal.'},
    {'nombre_empresa': 'Hotel Estrella', 'posicion': 'Mucama', 'salario': 90000, 'descripcion': 'Limpieza y orden de habitaciones.'}
]
for trabajo in trabajos:
    Trabajo.objects.get_or_create(**trabajo)

# Crear blogs
blogs = [
    {'titulo': 'Temporada de Verano', 'subtitulo': 'Actividades y eventos', 'cuerpo': 'Disfruta del sol y actividades al aire libre.', 'autor': User.objects.first()},
    {'titulo': 'Temporada de Invierno', 'subtitulo': 'Eventos y promociones', 'cuerpo': 'Disfruta del invierno con promociones únicas.', 'autor': User.objects.first()}
]
for blog in blogs:
    Blog.objects.get_or_create(**blog)

print("Datos cargados correctamente.")
