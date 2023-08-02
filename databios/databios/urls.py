from django.contrib import admin
from django.urls import path, include
from almacen.views import homeView,catalogo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('almacen.urls'), name='api'),
    path('admin/', admin.site.urls),
    path('', catalogo, name='Homeview'),
    path('catalogo/', catalogo, name='productos'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
