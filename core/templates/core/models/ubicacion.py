from django.db import models

class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=150)

    def __str__(self):
        return self.ubicacion
