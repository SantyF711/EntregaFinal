from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import FormularioRegistro, FormularioLogin, EditarPerfilForm

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
    else:
        form = FormularioRegistro()
    return render(request, 'accounts/registro.html', {'form': form})

class VistaLogin(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = FormularioLogin

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mis_recetas')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'accounts/editar_perfil.html', {'form': form})