from django.test import TestCase
from AppBlog.views import Cantante, Album, Concierto
# Create your tests here.


class ViewTestCase(TestCase):

    def test_crear_cantante(self):
        Cantante.objects.create(nombre="Cantante1")
        todos_los_cantantes = Cantante.objects.all()
        assert len(todos_los_cantantes) == 1
        assert todos_los_cantantes[0].nombre == "Cantante1"


    def test_crear_album(self):
        Album.objects.create(cant_temas="10")
        todos_los_albums = Album.objects.all()
        assert todos_los_albums[0].fecha_de_lanzamiento is None
        


    def test_concierto(self):
        Concierto.objects.create(lugar="Lugar_de_concierto")
        todos_los_conciertos = Concierto.objects.all()
        assert len(todos_los_conciertos) == 1
        assert todos_los_conciertos[0].lugar == "Lugar_de_concierto"