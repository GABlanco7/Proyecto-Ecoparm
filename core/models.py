from django.db import models

from core.templates.core.models.usuario import Usuario




class Zonas(models.Model):
    codigo_zonas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    responsable = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Emergencia(models.Model):
    codigo_e = models.AutoField(primary_key=True)
    tipo_e = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)
    fecha = models.CharField(max_length=45)
    gravedad = models.CharField(max_length=45)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.tipo_e} - {self.gravedad}"

class Evidencia(models.Model):
    codigo_evidencias = models.AutoField(primary_key=True)
    fecha = models.DateField()
    direccion = models.CharField(max_length=45)
    evidencias = models.TextField()
    evidencias_fotograficas = models.CharField(max_length=45)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Evidencia {self.codigo_evidencias}"

class FaunaYFlora(models.Model):
    TIPO_CHOICES = (
        ('Fauna', 'Fauna'),
        ('Flora', 'Flora'),
    )

    codigo = models.AutoField(primary_key=True)
    especie = models.CharField(max_length=10, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    caracteristicas = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class EvidenciasFaunaFlora(models.Model):
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fauna_flora = models.ForeignKey(FaunaYFlora, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evidencia', 'usuario', 'fauna_flora')

class Ubicacion(models.Model):
    codigo_ubicacion = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=45)
    evidencia = models.ForeignKey(Evidencia, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ubicacion
