from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def admin_page(request):
    return render(request, 'core/admin.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def guardaparamo(request):
    return render(request, 'core/guardaparamo.html')

def login_page(request):
    return render(request, 'core/login.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def recuperar_contraseña(request):
    return render(request, 'core/recuperar_contrasena.html')
