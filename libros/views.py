
from django.shortcuts import render, redirect
from .reservas import reservas_singleton

libros = [
    {'titulo': 'El Principito', 'autor': 'Antoine de Saint-Exupéry', 'imagen': '1.jpg'},
    {'titulo': '1984', 'autor': 'George Orwell', 'imagen': '2.jpg'},
    {'titulo': 'evangelio', 'autor': 'Hideaki Anno', 'imagen': '3.jpg'},
    {'titulo': 'Clean Code', 'autor': 'Robert C. Martin', 'imagen': '4.jpg'},
    {'titulo': 'The Pragmatic Programmer', 'autor': 'Andrew Hunt y David Thomas', 'imagen': '5.jpg'},
    {'titulo': 'Programación para Principiantes', 'autor': 'John Doe', 'imagen': '6.webp'},
    
]

def hola(request):
    return render(request, 'hola.html', {'libros': libros})

def index(request):
    return render(request, 'index.html', {'libros': libros})

def reservar(request, titulo):
    reservas_singleton.agregar_reserva(titulo)
    return redirect('index')

def mis_reservas(request):
    return render(request, 'mis_reservas.html', {'reservas': reservas_singleton.obtener_reservas()})
