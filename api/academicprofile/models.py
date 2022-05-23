from django.db import models

# Create your models here.
class aplicante(models.Model):
    codigo = models.CharField(max_length=3, primary_key= True)
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    institución = models.CharField(max_length=50)
    duración = models.CharField(max_length=50)
    Estatus = models.CharField(max_length=50)
