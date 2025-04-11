from django.db import models

from core.templates.core.models.evidencia import Evidencia

class FaunaFlora(models.Model):
    id = models.AutoField(primary_key=True)
    ESPECIE_CHOICES = [
        ("Fauna", "Fauna"),
        ("Flora", "Flora"),
    ]

    nombre = models.CharField(max_length=80)
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    estado = models.CharField(max_length=250)
    caracteristicas = models.CharField(max_length=300)
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"