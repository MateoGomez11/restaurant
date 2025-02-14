from django.db import models # type: ignore

# Create your models here.
class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    tipoproducto = models.CharField()
    descripproducto = models.CharField()
    imagenprodcuto = models.BinaryField(blank=True, null=True)
    estadoproducto = models.CharField()
    precioproducto = models.DecimalField(max_digits=10, decimal_places=0)
    nombreproducto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'producto'