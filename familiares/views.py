from django.shortcuts import render, get_object_or_404, redirect
from .models import Familiar, Amigo, Trabajo, Blog
from .forms import FamiliarForm, AmigoForm, TrabajoForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ====================
# VISTA PARA LA PÁGINA PRINCIPAL
# ====================
def index(request):
    """
    Página principal de la aplicación.
    """
    return render(request, 'familiares/index.html')


# ====================
# VISTA PARA REGISTRO DE USUARIOS (SIGNUP)
# ====================
def signup(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_familiares')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# ====================
# VISTAS PARA FAMILIARES
# ====================
@login_required
def lista_familiares(request):
    """
    Lista de todos los familiares registrados en la base de datos.
    """
    familiares = Familiar.objects.all().order_by('nombre')
    return render(request, 'familiares/lista_familiares.html', {'familiares': familiares})

@login_required
def agregar_familiar(request):
    """
    Agregar un nuevo familiar.
    """
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_familiares')
    else:
        form = FamiliarForm()
    return render(request, 'familiares/agregar_familiar.html', {'form': form})


@login_required
def editar_familiar(request, pk):
    """
    Editar un familiar existente.
    """
    familiar = get_object_or_404(Familiar, pk=pk)
    if request.method == 'POST':
        form = FamiliarForm(request.POST, instance=familiar)
        if form.is_valid():
            form.save()
            return redirect('lista_familiares')
    else:
        form = FamiliarForm(instance=familiar)
    return render(request, 'familiares/editar_familiar.html', {'form': form})


@login_required
def eliminar_familiar(request, pk):
    """
    Eliminar un familiar existente.
    """
    familiar = get_object_or_404(Familiar, pk=pk)
    if request.method == 'POST':
        familiar.delete()
        return redirect('lista_familiares')
    return render(request, 'familiares/eliminar_familiar.html', {'familiar': familiar})


# ====================
# VISTAS PARA AMIGOS
# ====================
@login_required
def lista_amigos(request):
    """
    Lista de todos los amigos registrados en la base de datos.
    """
    amigos = Amigo.objects.all().order_by('nombre')
    return render(request, 'familiares/lista_amigos.html', {'amigos': amigos})


# ====================
# VISTAS PARA TRABAJOS
# ====================
@login_required
def lista_trabajos(request):
    """
    Lista de todos los trabajos registrados en la base de datos.
    """
    trabajos = Trabajo.objects.all().order_by('nombre_empresa')
    return render(request, 'familiares/lista_trabajos.html', {'trabajos': trabajos})


# ====================
# VISTAS PARA BLOGS
# ====================
@login_required
def lista_blogs(request):
    """
    Lista de todas las publicaciones de blogs registradas en la base de datos.
    """
    blogs = Blog.objects.all().order_by('-fecha')
    return render(request, 'familiares/lista_blogs.html', {'blogs': blogs})

@login_required
def detalle_blog(request, pk):
    """
    Vista detallada de una entrada de blog.
    """
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'familiares/detalle_blog.html', {'blog': blog})
