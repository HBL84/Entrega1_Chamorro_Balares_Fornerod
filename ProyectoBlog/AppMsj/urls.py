from django.urls import path

from AppMsj.views import (
    mensajes,
)

urlpatterns = [path("", mensajes, name="inicio_msj")]
