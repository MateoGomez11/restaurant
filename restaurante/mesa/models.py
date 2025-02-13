from django.db import models # type: ignore

# Create your models here.
class Mesa(models.Model):
    idmesa = models.AutoField(primary_key=True)
    capmesa = models.SmallIntegerField()
    estadomesa = models.CharField()
    ubimesa = models.CharField()

    class Meta:
        db_table = 'mesa'