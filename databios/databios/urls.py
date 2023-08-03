from django.contrib import admin
from django.urls import path
from almacen.views import homeView,catalogo
from django.conf import settings
from django.conf.urls.static import static
from account.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalogo, name='Homeview'),
    path('catalogo/', catalogo, name='productos'),
    path('register/', register, name='registro'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
