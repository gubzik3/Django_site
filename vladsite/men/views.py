from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


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
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")