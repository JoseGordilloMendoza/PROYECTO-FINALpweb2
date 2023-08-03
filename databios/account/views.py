from django.shortcuts import render, redirect
from .forms import RegistrationForm
from almacen.views import catalogo

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(catalogo)  # Redirige a la página deseada después de un registro exitoso
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

