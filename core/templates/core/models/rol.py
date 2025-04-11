from django.db import models


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=80)

    def __str__(self):
        return self.rol