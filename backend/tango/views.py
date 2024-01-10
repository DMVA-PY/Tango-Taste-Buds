from django.shortcuts import render
from django.http import HttpResponse
 
# Views se refiere a las funciones o clases que manejan las solicitudes web y devuelven una respuesta.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def messi(request):
    return render(request, 'crud/messi.html')

def breakfast(request):
    return render(request, 'crud/breakfast.html')

def lunch(request):
    return render(request, 'crud/lunch.html')

def dinner(request):
    return render(request, 'crud/dinner.html')

