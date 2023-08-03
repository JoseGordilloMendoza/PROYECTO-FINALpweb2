from django.contrib import admin
from django.urls import path
from almacen.views import contactoView, blogView, verificacionView, detallesBlogView, carritoView, inicioView, homeView, catalogo, filtroproductosView, detalletiendaView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='Homeview'),    
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
