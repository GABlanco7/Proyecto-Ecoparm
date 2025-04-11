from django.db import models

from core.templates.core.models.ubicacion import Ubicacion
from core.templates.core.models.usuario import Usuario

class Evidencia(models.Model):
    id = models.AutoField(primary_key=True)
    caracteristicas = models.CharField(max_length=450)
    direccion = models.CharField(max_length=200)
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Evidencia #{self.id}"