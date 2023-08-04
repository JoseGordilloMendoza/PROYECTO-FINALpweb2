from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Product,Categoria
from django.urls import reverse_lazy


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



class ProductCreateView(CreateView):
    model = Product
    fields = ['categorias', 'nombre', 'descripcion', 'precio', 'imagen', 'stock']
    template_name = 'product_form.html'  # Nombre de la plantilla para el formulario de creación de producto
    success_url = '/'  # URL de redirección después de guardar un nuevo producto

    def form_valid(self, form):
        # Guarda el objeto del formulario antes de añadir la relación muchos a muchos
        product = form.save()

        # Obtiene las categorías seleccionadas en el formulario
        categorias = form.cleaned_data['categorias']
        
        # Añade las categorías seleccionadas al modelo Product
        product.categorias.set(categorias)
        
        return super().form_valid(form)
    
def product_list(request):
    # Obtener todos los productos
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['categorias', 'nombre', 'descripcion', 'precio', 'imagen', 'stock']
    template_name = 'product_edit.html'  # Nombre de la plantilla para el formulario de edición de producto
    success_url = '/'  # URL de redirección después de guardar los cambios en el producto

    def form_valid(self, form):
        # Realiza acciones adicionales antes de guardar los cambios en el producto (opcional)
        return super().form_valid(form)
    

def product_delete_list(request):
    # Obtener todos los productos
    products = Product.objects.all()
    return render(request, 'product_delete_list.html', {'products': products})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'  # Nombre de la plantilla para la confirmación de eliminación
    success_url = reverse_lazy('product_list')  # URL de redirección después de eliminar un producto

    def form_valid(self, form):
        # Realiza acciones adicionales antes de eliminar el producto (opcional)
        return super().form_valid(form)