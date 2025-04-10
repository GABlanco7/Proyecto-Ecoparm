from django.db import models

class Zona(models.Model):
    codigo_zonas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    responsable = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
