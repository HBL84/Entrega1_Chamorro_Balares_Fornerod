from django.contrib import admin
from AppBlog.models import Cantante, Album, Concierto, Articulo

# Register your models here.

admin.site.register(Cantante)
admin.site.register(Album)
admin.site.register(Concierto)
admin.site.register(Articulo)
