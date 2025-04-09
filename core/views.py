from django.shortcuts import render
from rest_framework import viewsets

from core.templates.core.models.rol import Rol
from .models import Usuario
from .serializers import RolSerializer, UsuarioSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rol
from .serializers import RolSerializer
from django.http import Http404

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


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class RolListCreateAPIView(APIView):
    def get(self, request):
        roles = Rol.objects.all()
        serializer = RolSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RolDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Rol.objects.get(pk=pk)
        except Rol.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rol = self.get_object(pk)
        serializer = RolSerializer(rol)
        return Response(serializer.data)

    def put(self, request, pk):
        rol = self.get_object(pk)
        serializer = RolSerializer(rol, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rol = self.get_object(pk)
        rol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
