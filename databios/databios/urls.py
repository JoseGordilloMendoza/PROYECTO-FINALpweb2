from django.contrib import admin
from django.urls import path
from almacen.views import homeView,catalogo
from django.conf import settings
from django.conf.urls.static import static
from account.views import register,login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='Homeview'),
    path('catalogo/', catalogo, name='productos'),
    path('register/', register, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
