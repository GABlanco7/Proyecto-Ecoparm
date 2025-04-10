from django.db import models

from core.templates.core.models.rol import Rol


class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.BigIntegerField()  # Cambiado a BigIntegerField
    correo = models.CharField(max_length=45)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    zona = models.ForeignKey('Zona', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
