from django.contrib import admin
from django.urls import path
from almacen.views import ProductAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', ProductAPI.as_view(), name='api'),
]  