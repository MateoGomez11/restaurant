from django.db import models

# Create your models here.
class Personal(models.Model):
    idpersonal = models.AutoField(primary_key=True)
    nombreper = models.CharField()
    apellidoper = models.CharField()
    puestoper = models.CharField()
    estadoper = models.CharField()

    class Meta:
        managed = False
        db_table = 'personal'