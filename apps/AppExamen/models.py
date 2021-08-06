from django.db import models

# Create your models here.

class Final(models.Model):
    pk_examen = models.AutoField(primary_key=True)
    alumno = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    grado = models.TextField(blank=False, null=True)