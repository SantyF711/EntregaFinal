from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Receta, Post
from .forms import RecetaForm, PostForm
from django.urls import reverse


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def ver_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_publicacion')
    return render(request, 'core/ver_recetas.html', {'recetas': recetas})

@login_required
def mis_recetas(request):
    recetas = request.user.recetas.all()
    return render(request, 'core/mis_recetas.html', {'recetas': recetas})

@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.usuario = request.user
            receta.save()
            return redirect('mis_recetas')
    else:
        form = RecetaForm()
    return render(request, 'core/crear_receta.html', {'form': form})

@login_required
def editar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('mis_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'core/editar_receta.html', {'form': form})

@login_required
def borrar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk, usuario=request.user)
    if request.method == 'POST':
        receta.delete()
        return redirect('mis_recetas')
    return render(request, 'core/borrar_receta.html', {'receta': receta})

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    posts = receta.posts.all().order_by('-fecha_publicacion')

    referer = request.GET.get('next') or request.POST.get('next') or request.META.get('HTTP_REFERER')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.usuario = request.user
            nuevo_post.receta = receta
            nuevo_post.save()
            if referer:
                return redirect(f'{reverse("detalle_receta", args=[receta.pk])}?next={referer}')
            else:
                return redirect('detalle_receta', pk=receta.pk)
    else:
        form = PostForm()

    return render(request, 'core/detalle_receta.html', {
        'receta': receta,
        'posts': posts,
        'form': form,
        'referer': referer,
    })

def recetas_buscar(request):
    query = request.GET.get('q', '')
    recetas = Receta.objects.all()
    if query:
        recetas = recetas.filter(
            Q(titulo__icontains=query) |
            Q(ingredientes__icontains=query) |
            Q(preparacion__icontains=query)
        )
    context = {
        'recetas': recetas,
        'query': query,
    }
    return render(request, 'core/ver_recetas.html', context)

@login_required
def eliminar_comentario(request, post_id):
    comentario = get_object_or_404(Post, id=post_id)
    if comentario.usuario == request.user:
        receta_id = comentario.receta.pk
        comentario.delete()
        return redirect('detalle_receta', pk=receta_id)
    return redirect('detalle_receta', pk=comentario.receta.pk)