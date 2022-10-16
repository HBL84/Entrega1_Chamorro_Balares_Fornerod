from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Album, Cantante, Concierto, Articulo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse


# Create your views here.


def inicio(request):
    return render(request, "AppBlog/inicio.html")


@login_required
def cantantes(request):
    cantantes = Cantante.objects.all()
    contexto = {"cantantes_encontrados": cantantes}
    return render(request, "AppBlog/cantantes.html", context=contexto)


@login_required
def albums(request):
    albums = Album.objects.all()
    contexto = {"albums_encontrados": albums}
    return render(request, "AppBlog/albums.html", context=contexto)


@login_required
def conciertos(request):
    conciertos = Concierto.objects.all()
    contexto = {"conciertos_encontrados": conciertos}
    return render(request, "AppBlog/conciertos.html", context=contexto)


@login_required
def articulos(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos_encontrados": articulos}
    return render(request, "AppBlog/articulos.html", context=contexto)


@login_required
def formularios(request):
    return render(request, "AppBlog/formularios.html")


@login_required
def procesar_form_album(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_albums.html")

    album = Album(
        nombre=request.POST.get("nombreAlbum", "Temp"),
        cant_temas=request.POST.get("cantidadDeTemas", 10),
        fecha_de_lanzamiento=request.POST.get("fechaDeLanzamiento", "2020-10-20"),
    )

    album.save()
    return render(request, "AppBlog/inicio.html")


@login_required
def procesar_form_cantante(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_cantantes.html")

    cantante = Cantante(
        nombre=request.POST["nombre"],
        apellido=request.POST["apellido"],
        fecha_nacimiento=request.POST["fecha_de_nacimiento"],
        email=request.POST["email"],
    )

    cantante.save()
    return render(request, "AppBlog/inicio.html")


@login_required
def procesar_form_concierto(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_conciertos.html")

    concierto = Concierto(
        nombre=request.POST["nombre"],
        lugar=request.POST["lugar"],
        fecha_de_concierto=request.POST["fechaDelConcierto"],
    )

    concierto.save()
    return render(request, "AppBlog/inicio.html")


@login_required
def procesar_form_articulo(request):
    if request.method != "POST":
        return render(request, "AppBlog/form_articulos.html")

    articulo = Articulo(
        nombre=request.POST["nombre"],
        texto=request.POST["articulo"],
        fecha=request.POST["fechaDelArticulo"],
    )

    articulo.save()
    return render(request, "AppBlog/inicio.html")


@login_required
def busqueda(request):
    return render(request, "AppBlog/busqueda.html")


@login_required
def buscar(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        cantantes = Cantante.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "cantantes_encontrados": cantantes}

        return render(request, "AppBlog/resultado_busqueda.html", contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(
                    request, "AppBlog/inicio.html", {"mensaje": f"Bienvenido {usuario}"}
                )
            else:
                return render(
                    request,
                    "AppBlog/inicio.html",
                    {"mensaje": "Error, datos incorrectos"},
                )

        else:
            return render(
                request, "AppBlog/inicio.html", {"mensaje": "Error, formulario erróneo"}
            )

    form = AuthenticationForm()

    return render(request, "AppBlog/login.html", {"form": form})


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "AppBlog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "AppBlog/registro.html", {"form": form})


class AlbumDelete(DeleteView, LoginRequiredMixin):

    model = Album
    success_url = "/AppBlog/albums"


class ArticuloDelete(DeleteView, LoginRequiredMixin):

    model = Articulo
    success_url = "/AppBlog/articulos"


class CantanteDelete(DeleteView, LoginRequiredMixin):

    model = Cantante
    success_url = "/AppBlog/cantantes"


class ConciertoDelete(DeleteView, LoginRequiredMixin):

    model = Concierto
    success_url = "/AppBlog/conciertos"


# Detail Views


class AlbumDetail(DetailView, LoginRequiredMixin):

    model = Album
    template_name = "AppBlog/album_detalle.html"


class ArticuloDetail(DetailView, LoginRequiredMixin):

    model = Articulo
    template_name = "AppBlog/articulo_detalle.html"


class CantanteDetail(DetailView, LoginRequiredMixin):

    model = Cantante
    template_name = "AppBlog/cantante_detalle.html"


class ConciertoDetail(DetailView, LoginRequiredMixin):

    model = Concierto
    template_name = "AppBlog/concierto_detalle.html"


# Listar Views


class AlbumList(ListView):
    model = Album
    template_name: "AppBlog/albums_lista.html"


class CantanteList(ListView):
    model = Cantante
    template_name: "AppBlog/cantantes_lista.html"


class ConciertoList(ListView):
    model = Concierto
    template_name: "AppBlog/conciertos_lista.html"


class ArticuloList(ListView):
    model = Articulo
    template_name: "AppBlog/articulos_lista.html"


# Create view


class AlbumCreacion(CreateView):
    model = Album
    fields = ["nombre", "banda"]

    def get_success_url(self):
        return reverse("AlbumLista")


class CantanteCreacion(CreateView):
    model = Cantante
    fields = ["nombre", "banda"]

    def get_success_url(self):
        return reverse("Cantantelista")


class ConciertoCreacion(CreateView):
    model = Concierto
    fields = ["fecha", "banda"]

    def get_success_url(self):
        return reverse("Conciertolista")


class ArticuloCreacion(CreateView):
    model = Articulo
    fields = ["nombre"]

    def get_success_url(self):
        return reverse("Articulolista")


# Update view

class AlbumUpdateView(UpdateView, LoginRequiredMixin):
    model = Album
    #success_url = "AppBlog/albums"
    fields = ["nombre", "cant_temas", "fecha_de_lanzamiento"]

    def get_success_url(self):
        return reverse("albums")


class CantanteUpdateView(UpdateView):
    model = Cantante
    fields = ["nombre", "banda"]

    def get_success_url(self):
        return reverse("Cantantelista")


class ConciertoUpdateView(UpdateView):
    model = Concierto
    fields = ["fecha", "banda"]

    def get_success_url(self):
        return reverse("Conciertolista")


class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ["nombre", "banda"]

    def get_success_url(self):
        return reverse("Articulolista")
