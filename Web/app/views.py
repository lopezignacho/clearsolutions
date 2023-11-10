from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def servicios(request):
    return render(request, 'app/servicios.html')

def contacto(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        send_mail('Formulario Contacto ' + subject, name + ' ' + email + ' ' + message,
                  'patricio.antonio.salvo@gmail.com', ['patricio.antonio.salvo@gmail.com'], fail_silently=False)
        # Aquí podrías agregar una redirección a una página de éxito o a la página de inicio
        return render(request, 'app/home.html')
    # Si es una solicitud GET (cuando se carga la página normalmente), simplemente renderiza el formulario de contacto
    return render(request, 'app/contacto.html')
