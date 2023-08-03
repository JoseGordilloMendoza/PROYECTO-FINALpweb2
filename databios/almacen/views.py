from django.shortcuts import render
from .models import Product,Categoria
def homeView(request):
    return render(request, 'index.html')


def catalogo(request):
    obj = Product.objects.all()
    categorias = Categoria.objects.all()
    context ={
      'productos': obj,
      'categorias': categorias,
    }
    return render(request, 'catalogo.html', context)