from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Album, Cantante, Concierto, Articulo

# Create your views here.


def inicio(request):
    return render(request, "AppBlog/inicio.html")


def cantantes(request):
    cantantes = Cantante.objects.all()
    contexto = {"cantantes_encontrados": cantantes}
    return render(request, "AppBlog/cantantes.html", context=contexto)

def albums(request):
    albums = Album.objects.all()
    contexto = {"albums_encontrados": albums}
    return render(request, "AppBlog/albums.html", context=contexto)

def conciertos(request):
    conciertos = Concierto.objects.all()
    contexto = {"conciertos_encontrados": conciertos}
    return render(request, "AppBlog/conciertos.html", context=contexto)

def articulos(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos_encontrados": articulos}
    return render(request, "AppBlog/articulos.html", context=contexto)

def formularios(request):
    return render(request, "AppBlog/formularios.html")

def procesar_form_album(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_albums.html")

    album = Album(nombre=request.POST.get("nombreAlbum", "Temp"), 
                 cant_temas = request.POST.get("cantidadDeTemas", 10),
                 fecha_de_lanzamiento = request.POST.get("fechaDeLanzamiento", '2020-10-20'))

    album.save()
    return render(request, "AppBlog/inicio.html")

def procesar_form_cantante(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_cantantes.html")

    cantante = Cantante(nombre=request.POST["nombre"],
                        apellido=request.POST["apellido"],
                        fecha_nacimiento=request.POST["fecha_de_nacimiento"],
                        email=request.POST["email"],
    )

    cantante.save()
    return render(request, "AppBlog/inicio.html")

def procesar_form_concierto(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_conciertos.html")

    concierto = Concierto(nombre=request.POST["nombre"],
                          lugar=request.POST["lugar"],
                          fecha_de_concierto=request.POST["fechaDelConcierto"]
    )

    concierto.save()
    return render(request, "AppBlog/inicio.html")

def procesar_form_articulo(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_articulos.html")

    articulo = Articulo(nombre=request.POST["nombre"],
                        texto=request.POST["articulo"],
                        fecha=request.POST["fechaDelArticulo"],
    )

    articulo.save()
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
