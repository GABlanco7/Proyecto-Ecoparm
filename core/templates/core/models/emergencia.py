from django.db import models

from core.templates.core.models.usuario import Usuario

class Emergencia(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=150)
    gravedad = models.CharField(max_length=250)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Emergencia: {self.tipo} - {self.gravedad}"