from django.db import models

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)
    idestado = models.IntegerField()
