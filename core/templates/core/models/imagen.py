from django.db import models

from core.templates.core.models.evidencia import Evidencia

class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250)
    link_imagen = models.CharField(max_length=250)
    fecha = models.DateTimeField()
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre