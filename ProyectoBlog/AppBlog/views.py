from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def cantantes(request):
    return render(request, "AppBlog/cantantes.html")

def albums(request):
    return render(request, "AppBlog/albums.html")

def conciertos(request):
    return render(request, "AppBlog/conciertos.html")