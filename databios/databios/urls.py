from django.contrib import admin
from django.urls import path
from almacen.views import homeView,filtroCategoria
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='Homeview'),
    path('filtroCategoria/',filtroCategoria, name='productos'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
