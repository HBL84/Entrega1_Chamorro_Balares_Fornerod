from django.shortcuts import render
from AppBlog.models import Album, Cantante, Concierto, Articulo

# Create your views here.

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def cantantes(request):
    return render(request, "AppBlog/cantantes.html")

def albums(request):
    return render(request, "AppBlog/albums.html")

def conciertos(request):
    return render(request, "AppBlog/conciertos.html")


def procesar_formulario(request):
    if request.method !="POST":
        return render (request, "AppBlog/inicio.html" )

    album = Album(nombre=request.POST["albums"])

    album.save()
    return render (request, "AppBlog/inicio.html") 


def procesar_formulario_2(request):
    if request.method !="POST":
        return render (request, "AppBlog/inicio.html" )

    album = Cantante(nombre=request.POST["cantantes"])

    album.save()
    return render (request, "AppBlog/inicio.html") 


def procesar_formulario_3(request):
    if request.method !="POST":
        return render (request, "AppBlog/inicio.html" )

    album = Concierto(nombre=request.POST["conciertos"])

    album.save()
    return render (request, "AppBlog/inicio.html") 


def procesar_formulario_4(request):
    if request.method !="POST":
        return render (request, "AppBlog/inicio.html" )

    album = Articulo(nombre=request.POST["articulos"])

    album.save()
    return render (request, "AppBlog/inicio.html") 