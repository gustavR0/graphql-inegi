from django.db import models
from django.conf import settings

class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    idestado = models.ForeignKey('estados.Estado', related_name='estados', on_delete=models.CASCADE)
    idmunicipio = models.IntegerField()
    municipio = models.CharField(max_length=80)