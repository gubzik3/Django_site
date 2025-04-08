from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения men")

def name_men(request):
    return HttpResponse("<h1>Мужчины по именам<h1>")

def proverka(request, menid):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>Проверочный запрос<h1><p>{menid}<p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")