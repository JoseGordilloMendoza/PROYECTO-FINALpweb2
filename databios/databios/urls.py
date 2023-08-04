from django.contrib import admin
from django.urls import path
from almacen.views import homeView,catalogo, ProductDeleteView,ProductCreateView,ProductUpdateView, product_list, product_delete_list
from django.conf import settings
from django.conf.urls.static import static
from account.views import register, loginView, logout
from almacen.views  import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='Homeview'),
    path('catalogo/', catalogo, name='productos'),
    path('register/', register, name='registro'),
    path('login/', loginView, name='login'),
    path('logout/', logout, name='logout'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/list/', product_list, name='product_list'),
    path('product/delete/list/', product_delete_list, name='product_delete_list'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalogo/', catalogo, name='productos'),
    path('inicio/', inicioView, name='inicio'),
    path('filtroproductos/', filtroproductosView, name='filtroproductos'),
    path('detalletienda/', detalletiendaView, name='detalletienda'),
    path('carrito/', carritoView, name='carrito'),
    path('detallesBlog/', detallesBlogView, name='detallesBlog'),
    path('verificacion/', verificacionView, name='verificacion'),
    path('blog/', blogView, name='blog'),
    path('contacto/', contactoView, name='contacto'),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
