from django.shortcuts import render
from .models import Product,Categoria
from rest_framework import generics
from .serializer import ProductSerializer

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

class ProductAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        categorias_especificas = self.request.query_params.getlist('categorias')
        queryset = Product.objects.all()

        for categoria in categorias_especificas:
            queryset = queryset.filter(categorias__nombre=categoria)

        return queryset