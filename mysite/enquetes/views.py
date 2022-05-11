from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(
        "<ul><li>Nome: Lucas Oliveira Véras</li><li>Matrícula: 20211014040015</li</ul>"
    )