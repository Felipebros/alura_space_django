from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def index_outra_maneira(request):
    return HttpResponse("<h1>Outra maneira de printar um html</h1>")
