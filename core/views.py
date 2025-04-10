from django.shortcuts import render
from rest_framework import generics

from core.templates.core.models.rol import Rol
from core.templates.core.models.usuario import Usuario
from core.templates.core.models.zona import Zona
from .serializers import RolSerializer, UsuarioSerializer, ZonaSerializer


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
#rol
class RolListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()  # Obtiene todos los roles
    serializer_class = RolSerializer  # Usa el serializador creado

class RolDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()  # Obtiene el rol por su ID
    serializer_class = RolSerializer  # Usa el serializador creado
#zona
class ZonaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zona.objects.all()  
    serializer_class = ZonaSerializer

class ZonaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zona.objects.all()  
    serializer_class = ZonaSerializer 

#usuario
class UsuarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer

class UsuarioDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer 

