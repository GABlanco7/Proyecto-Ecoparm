# core/serializers.py
from rest_framework import serializers

from core.templates.core.models.rol import Rol
from core.templates.core.models.usuario import Usuario
from core.templates.core.models.zona import Zona


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'



class UsuarioSerializer(serializers.ModelSerializer):
    zona = serializers.PrimaryKeyRelatedField(queryset=Zona.objects.all())
    rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all())

    class Meta:
        model = Usuario
        fields = '__all__'