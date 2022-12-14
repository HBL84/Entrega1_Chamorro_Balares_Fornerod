#from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Album, Cantante, Concierto, Articulo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Agregado para avatar
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse

from AppBlog.forms import UserRegisterForm, UserEditionForm

from AppBlog.models import Avatar

from AppBlog.forms import AvatarForm, UserEditionForm


# Create your views here.


def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except:
        avatar = None
    return render(request, "AppBlog/padre.html", {"avatar": avatar})


@login_required
def about(request):
    return render(request, "AppBlog/about.html")


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
    return albums(request)


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
    return cantantes(request)


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
    return conciertos(request)


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
    return articulos(request)


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
                    request,
                    "AppBlog/inicio.html",
                )
            else:
                return render(
                    request,
                    "AppBlog/login_error.html",
                    {"mensaje": "Datos Incorrectos. Intente nuevamente."},
                )

        else:
            return render(
                request,
                "AppBlog/login_error.html",
                {"mensaje": "Datos Incorrectos. Intente nuevamente."},
            )

    form = AuthenticationForm()

    return render(request, "AppBlog/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "AppBlog/registro_ok.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserRegisterForm()

    return render(request, "AppBlog/registro.html", {"form": form})


class AlbumDelete(LoginRequiredMixin, DeleteView):

    model = Album
    success_url = "/AppBlog/albums"


class ArticuloDelete(LoginRequiredMixin, DeleteView):

    model = Articulo
    success_url = "/AppBlog/articulos"


class CantanteDelete(LoginRequiredMixin, DeleteView):

    model = Cantante
    success_url = "/AppBlog/cantantes"


class ConciertoDelete(LoginRequiredMixin, DeleteView):

    model = Concierto
    success_url = "/AppBlog/conciertos"


# Detail Views


class AlbumDetail(LoginRequiredMixin, DetailView):

    model = Album
    template_name = "AppBlog/album_detalle.html"


class ArticuloDetail(LoginRequiredMixin, DetailView):

    model = Articulo
    template_name = "AppBlog/articulo_detalle.html"


class CantanteDetail(LoginRequiredMixin, DetailView):

    model = Cantante
    template_name = "AppBlog/cantante_detalle.html"


class ConciertoDetail(LoginRequiredMixin, DetailView):

    model = Concierto
    template_name = "AppBlog/concierto_detalle.html"


# Update view


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ["nombre", "cant_temas", "fecha_de_lanzamiento"]

    def get_success_url(self):
        return reverse("albums")


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ["nombre", "texto", "fecha"]

    def get_success_url(self):
        return reverse("articulos")


class CantanteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cantante
    fields = ["nombre", "apellido", "fecha_nacimiento", "email"]

    def get_success_url(self):
        return reverse("cantantes")


class ConciertoUpdateView(LoginRequiredMixin, UpdateView):
    model = Concierto
    fields = ["nombre", "lugar", "fecha_de_concierto"]

    def get_success_url(self):
        return reverse("conciertos")


# Editar Perfil


@login_required
def editar_perfil(request):
    user = request.user

    if request.method == "POST":
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.password1 = data["password1"]
            user.password2 = data["password2"]
            user.save()

            return render(
                request,
                "AppBlog/editarPerfil_ok.html",
                {"mensaje": f"Usuario: {user.username}"},
            )

    else:
        form = UserEditionForm(
            initial={
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        )

    contexto = {"user": user, "form": form}
    return render(request, "AppBlog/editarPerfil.html", contexto)


# Avatar


@login_required
def agregar_avatar(request):
    user = request.user

    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return inicio(request)

    contexto = {"form": form}
    return render(request, "AppBlog/avatar_form.html", contexto)
