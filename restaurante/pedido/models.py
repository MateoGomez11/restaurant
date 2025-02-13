from django.db import models
from mesa.models import Mesa
from personal.models import Personal
from producto.models import Producto 
# Create your models here.
class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idmesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='idmesa')
    idpersonal = models.ForeignKey(Personal, models.DO_NOTHING, db_column='idpersonal')
    fechahoraped = models.DateTimeField()
    estadoped = models.CharField()
    subtotalped = models.DecimalField(max_digits=65535, decimal_places=65535)
    descuentoped = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    comentariosped = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Pedidoxproducto(models.Model):
    idpedidoxproducto = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto')
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    cantproducto = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'pedidoxproducto'