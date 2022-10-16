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
from django.contrib.auth.views import LogoutView

from AppBlog.views import (
    AlbumDelete,
    ArticuloDelete,
    CantanteDelete,
    ConciertoDelete,
    AlbumDetail,
    ArticuloDetail,
    CantanteDetail,
    ConciertoDetail,
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
    login_request,
    registro,
)
from ProyectoBlog.AppBlog.views import AlbumCreacion, AlbumList, AlbumUpdateView, ArticuloCreacion, ArticuloList, ArticuloUpdateView, CantanteCreacion, CantanteList, CantanteUpdateView, ConciertoCreacion, ConciertoList, ConciertoUpdateView


urlpatterns = [
    path("", inicio, name="inicio"),
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
    path("login/", login_request, name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="AppBlog/logout.html"),
        name="logout",
    ),
    path("registro/", registro, name="registro"),
    path("borrar_album/<pk>", AlbumDelete.as_view(), name="AlbumDelete"),
    path("borrar_articulo/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    path("borrar_cantante/<pk>", CantanteDelete.as_view(), name="CantanteDelete"),
    path("borrar_concierto/<pk>", ConciertoDelete.as_view(), name="ConciertoDelete"),
    path("detalle_album/<pk>", AlbumDetail.as_view(), name="AlbumDetail"),
    path("detalle_articulo/<pk>", ArticuloDetail.as_view(), name="ArticuloDetail"),
    path("detalle_cantante/<pk>", CantanteDetail.as_view(), name="CantanteDetail"),
    path("detalle_concierto/<pk>", ConciertoDetail.as_view(), name="ConciertoDetail"),
    path("albums_lista<pk>", AlbumList.as_view(), name="Albumlista" ),
    path("cantantes_lista<pk>", CantanteList.as_view(), name="Cantantelista" ),
    path("albums_lista<pk>", ConciertoList.as_view(), name="Conciertolista" ),
    path("albums_lista<pk>", ArticuloList.as_view(), name="Articulolista" ),
    path("curso-nuevo/", AlbumCreacion.as_view(), name="AlbumNew"),
    path("curso-nuevo/", CantanteCreacion.as_view(), name="CantanteNew"),
    path("curso-nuevo/", ConciertoCreacion.as_view(), name="ConciertoNew"),
    path("curso-nuevo/", ArticuloCreacion.as_view(), name="ArticuloNew"),
    path("editar/<pk>", AlbumUpdateView.as_view(), name="AlbumUpdate"),
    path("editar/<pk>", CantanteUpdateView.as_view(), name="CantanteUpdate"),
    path("editar/<pk>", ConciertoUpdateView.as_view(), name="ConciertoUpdate"),
    path("editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
]
