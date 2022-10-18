from django.shortcuts import render

# Create your views here.


def mensajes(request):
    return render(request, "AppMsj/mensajes.html")
