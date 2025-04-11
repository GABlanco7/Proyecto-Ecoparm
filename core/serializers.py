# core/serializers.py
from rest_framework import serializers

from core.templates.core.models.emergencia import Emergencia
from core.templates.core.models.evidencia import Evidencia
from core.templates.core.models.faunaflora import FaunaFlora
from core.templates.core.models.imagen import Imagen
from core.templates.core.models.rol import Rol
from core.templates.core.models.ubicacion import Ubicacion
from core.templates.core.models.usuario import Usuario
from core.templates.core.models.zona import Zona

#Rol
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

#Zona
class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'

#Usuatio
class UsuarioSerializer(serializers.ModelSerializer):
    zona = ZonaSerializer(read_only=True)
    zona_id = serializers.PrimaryKeyRelatedField(
        queryset=Zona.objects.all(), write_only=True, source='zona'
    )
    rol = RolSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(), write_only=True, source='rol'
    )

    class Meta:
        model = Usuario
        fields = [
            'id', 'cedula', 'nombre', 'apellido', 'telefono',
            'correo', 'contraseña', 'rol', 'rol_id', 'zona', 'zona_id'
        ]

#Ubicacion
class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

#evidencia
class EvidenciaSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer(read_only=True)
    ubicacion = UbicacionSerializer(read_only=True)

    class Meta:
        model = Evidencia
        fields = '__all__'


#Fauna y flora
class FaunaFloraSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaunaFlora
        fields = '__all__'

#Imagen
class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

#Emergencia
class Emergenciaerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergencia
        fields = '__all__'

