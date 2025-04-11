from django.db import models

class Zona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    responsable = models.CharField(max_length=80)
    ubicacion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre