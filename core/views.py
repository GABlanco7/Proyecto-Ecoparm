from django.shortcuts import render
from rest_framework import generics

from core.templates.core.models.rol import Rol
from .serializers import RolSerializer


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

class RolListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()  # Obtiene todos los roles
    serializer_class = RolSerializer  # Usa el serializador creado