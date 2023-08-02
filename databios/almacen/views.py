from django.shortcuts import render
from .models import product

def homeView(request):
    obj = product.objects.all()
    categorias = []
    for producto in obj:
        if producto.categoria not in categorias :
            categorias.append(producto.categoria)
    context ={
      'productos': obj,
      'categorias': categorias,
    }
    return render(request, 'index.html', context)

def filtroCategoria(request):
    categoria = request.GET.get('categoria')
    if categoria == 'Todos':
        productos = product.objects.all()
    else:
        productos = product.objects.filter(categoria=categoria)
    context = {
        'productos': productos
    }
    return render(request, 'categorias.html', context)