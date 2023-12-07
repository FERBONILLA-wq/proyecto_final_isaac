from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Bebida

@csrf_exempt
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            mensaje_error = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
            return render(request, 'registration/login.html', {'mensaje_error': mensaje_error})

    return render(request, 'registration/login.html')

def home(request):
    # Obtén todas las bebidas de la base de datos
    bebidas = Bebida.objects.all()
    mensaje_bienvenida = "¡Bienvenido a nuestra cafetería!"
    return render(request, 'home.html', {'mensaje_bienvenida': mensaje_bienvenida, 'bebidas': bebidas})
