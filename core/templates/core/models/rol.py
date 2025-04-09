from django.db import models

# Create your models here.
class Rol(models.Model):
    codigo_roles = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=45)

    def __str__(self):
        return self.rol