from django.shortcuts import render
from .models import Product, Categoria


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

def inicioView(request):
    return render(request, 'inicio.html')

def filtroproductosView(request):
    return render(request, 'filtroproductos.html')

def detalletiendaView(request):
    return render(request, 'detalletienda.html')

def carritoView(request):
    return render(request, 'carrito.html')

def detallesBlogView(request):
    return render(request, 'detallesBlog.html')

def verificacionView(request):
    return render(request, 'verificacion.html')

def blogView(request):
    return render(request, 'blog.html')

def contactoView(request):
    return render(request, 'contacto.html')