# core/serializers.py
from rest_framework import serializers

from core.templates.core.models.rol import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'