from django.urls import path

from AppMsj.views import (
    messages,
)

urlpatterns = [path("messages/", messages, name="messages")]
