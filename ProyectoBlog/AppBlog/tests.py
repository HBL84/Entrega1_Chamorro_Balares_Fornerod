from django.test import TestCase
from AppBlog.views import Cantante, Album, Concierto
# Create your tests here.


class ViewTestCase(TestCase):

    def test_crear_cantante(self):
        todos_los_cantantes_pre = Cantante.objects.all()
        cant_cantantes_pre = len(todos_los_cantantes_pre) + 1
        Cantante.objects.create(nombre="Cantante_test")
        todos_los_cantantes_pos = Cantante.objects.all()
        cant_cantates_pos = len(todos_los_cantantes_pos)
        assert cant_cantantes_pre == cant_cantates_pos
        assert todos_los_cantantes_pos[cant_cantantes_pre-1].nombre == "Cantante_test"


    def test_crear_album(self):
        todos_los_albums_pre = Album.objects.all()
        cant_todos_los_albums_pre = len(todos_los_albums_pre) + 1
        Album.objects.create(nombre="album_test", cant_temas= 10)
        todos_los_albums_pos = Album.objects.all()
        cant_todos_los_albums_pos = len(todos_los_albums_pos)
        assert cant_todos_los_albums_pre == cant_todos_los_albums_pos
        assert todos_los_albums_pos[cant_todos_los_albums_pre-1].nombre == "album_test"
        


    def test_concierto(self):
        todos_los_conciertos_pre = Concierto.objects.all()
        cant_todos_los_conciertos_pre = len(todos_los_conciertos_pre) + 1 
        Concierto.objects.create(nombre="Lugar_de_concierto_test")
        todos_los_conciertos_pos = Concierto.objects.all()
        cant_todos_los_conciertos_pos = len(todos_los_conciertos_pos)
        assert cant_todos_los_conciertos_pre == cant_todos_los_conciertos_pos
        assert todos_los_conciertos_pos[cant_todos_los_conciertos_pre-1].nombre == "Lugar_de_concierto_test"


test_1 = ViewTestCase()

test_1.test_crear_cantante()
test_1.test_crear_album()
test_1.test_concierto()