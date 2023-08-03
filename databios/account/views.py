from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .forms import CustomAuthenticationForm
from .models import CustomUser


from .forms import RegistrationForm
from almacen.views import homeView

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homeView)  # Redirige a la página deseada después de un registro exitoso
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = CustomUser.authenticate(username=username, password=password)

        if user is not None:
            CustomUser.login(request, user)
            return redirect(homeView)
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(homeView)
