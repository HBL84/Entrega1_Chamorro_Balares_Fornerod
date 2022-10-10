"""ProyectoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppBlog.views import (
    inicio,
    cantantes,
    conciertos,
    albums,
    articulos,
    procesar_form_album,
    procesar_form_cantante,
    procesar_form_concierto,
    procesar_form_articulo,
    busqueda,
    buscar,
    formularios,
)


urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("cantantes/", cantantes, name="cantantes"),
    path("conciertos/", conciertos, name="conciertos"),
    path("albums/", albums, name="albums"),
    path("articulos/", articulos, name="articulos"),
    path("form_albums/", procesar_form_album, name="form_albums"),
    path("form_cantantes/", procesar_form_cantante, name="form_cantantes"),
    path("form_conciertos/", procesar_form_concierto, name="form_conciertos"),
    path("form_articulos/", procesar_form_articulo, name="form_articulos"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
    path("formularios/", formularios, name="formularios"),
]
