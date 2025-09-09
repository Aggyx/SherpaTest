from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
import json

def login_web_view(request):
    """
    Web view for login form
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido, {user.username}!')
                return redirect('user-list')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')
    
    return render(request, 'auth/login.html')

def register_web_view(request):
    """
    Web view for registration form
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if not username or not password or not password_confirm:
            messages.error(request, 'Por favor, completa todos los campos.')
            return render(request, 'auth/register.html')
        
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return render(request, 'auth/register.html')
        
        try:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, f'¡Usuario {username} creado exitosamente!')
            return redirect('auth-login')
        except Exception as e:
            messages.error(request, f'Error al crear el usuario: {str(e)}')
    
    return render(request, 'auth/register.html')

@login_required
def user_list_web_view(request):
    """
    Web view for user list
    """
    users = User.objects.all().order_by('date_joined')
    return render(request, 'users/user_list.html', {'users': users})

def logout_web_view(request):
    """
    Web view for logout
    """
    auth_logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('api-index')
