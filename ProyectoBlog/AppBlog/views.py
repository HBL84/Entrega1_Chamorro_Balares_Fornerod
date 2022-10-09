from django.http import HttpResponse
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


def articulos(request):
    return render(request, "AppBlog/articulos.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_albums.html")

    album = Album(nombre=request.POST["albums"])

    album.save()
    return render(request, "AppBlog/inicio.html")


def procesar_formulario_2(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_cantantes.html")

    album = Cantante(nombre=request.POST["cantantes"])

    album.save()
    return render(request, "AppBlog/inicio.html")


def procesar_formulario_3(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_conciertos.html")

    album = Concierto(nombre=request.POST["conciertos"])

    album.save()
    return render(request, "AppBlog/inicio.html")


def procesar_formulario_4(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_articulos.html")

    album = Articulo(nombre=request.POST["articulos"])

    album.save()
    return render(request, "AppBlog/inicio.html")


def busqueda(request):
    return render(request, "AppBlog/busqueda.html")


def buscar(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        cantantes = Cantante.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "cantantes_encontrados": cantantes}

        return render(request, "AppBlog/resultado_busqueda.html", contexto)
