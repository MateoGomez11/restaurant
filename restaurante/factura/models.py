from django.db import models  # type: ignore

from pedido.models import Pedido
from personal.models import Personal

# Create your models here.
class Factura(models.Model):
    idfactura = models.AutoField(primary_key=True)
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    idpersonal = models.ForeignKey(Personal, models.DO_NOTHING, db_column='idpersonal')
    ivafactura = models.DecimalField(max_digits=65535, decimal_places=65535)
    propinafactura = models.DecimalField(max_digits=65535, decimal_places=65535)
    montofactura = models.DecimalField(max_digits=65535, decimal_places=65535)
    fechafactura = models.DateTimeField()
    formapagofactura = models.CharField()

    class Meta:
        db_table = 'factura'