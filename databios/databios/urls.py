from django.contrib import admin
from django.urls import path
from almacen.views import inicioView, homeView,filtroCategoria
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='Homeview'),    
    path('catalogo/',filtroCategoria, name='catalogo'),
    path('inicio/', inicioView, name='inicio'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
