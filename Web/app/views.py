from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def servicios(request):
    return render(request, 'app/servicios.html')

def contacto(request):
    return render(request, 'app/contacto.html')