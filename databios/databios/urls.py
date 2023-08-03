from django.contrib import admin
from django.urls import path
from almacen.views import inicioView, homeView, catalogo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='Homeview'),    
    path('catalogo/', catalogo, name='productos'),
    path('inicio/', inicioView, name='inicio'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
