from django.db import models

from core.templates.core.models.rol import Rol
from core.templates.core.models.zona import Zona


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cedula = models.CharField(max_length=12)
    telefono = models.CharField(max_length=13)
    correo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=60)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
