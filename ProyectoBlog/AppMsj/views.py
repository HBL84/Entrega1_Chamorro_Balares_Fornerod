from django.shortcuts import render

# Create your views here.


def messages(request):
    return render(request, "AppMsj/messages.html")
