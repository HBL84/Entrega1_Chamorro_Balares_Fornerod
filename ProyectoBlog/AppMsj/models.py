from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Mensajes(models.Model):
    texto_mensaje = models.CharField(max_length=40)

    class Meta: verbose_name_plural = "Mensajes"
