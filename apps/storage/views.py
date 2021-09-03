from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def detalles(request):
    return render(request, 'detalles.html')

def detalles2(request):
    return render(request, 'detalles2.html')