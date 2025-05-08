from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    data = {
        'title': 'App Medica',
        'description': 'Gesion de citas medicas',
        'author': 'Daniel Vera',
        'year': 2025,
    }
    return render(request, 'home.html', data)

def doctor_list(request):
    return HttpResponse("Lista de doctores")

def doctor_create(request):
    return HttpResponse("Crear doctor")
