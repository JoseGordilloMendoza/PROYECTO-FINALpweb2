from django.contrib import admin
from .models import Product, Categoria


class ProductAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'stock', 'user', 'created', 'modify']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

admin.site.register(Product, ProductAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'user', 'created', 'modify']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

admin.site.register(Categoria, CategoriaAdmin)