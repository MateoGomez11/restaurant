# Generated by Django 5.1.6 on 2025-02-13 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mesa', '0001_initial'),
        ('personal', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idpedido', models.AutoField(primary_key=True, serialize=False)),
                ('fechahoraped', models.DateTimeField()),
                ('estadoped', models.CharField()),
                ('subtotalped', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('descuentoped', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('comentariosped', models.CharField(blank=True, null=True)),
                ('idmesa', models.ForeignKey(db_column='idmesa', on_delete=django.db.models.deletion.DO_NOTHING, to='mesa.mesa')),
                ('idpersonal', models.ForeignKey(db_column='idpersonal', on_delete=django.db.models.deletion.DO_NOTHING, to='personal.personal')),
            ],
            options={
                'db_table': 'pedido',
            },
        ),
        migrations.CreateModel(
            name='Pedidoxproducto',
            fields=[
                ('idpedidoxproducto', models.AutoField(primary_key=True, serialize=False)),
                ('cantproducto', models.SmallIntegerField()),
                ('idpedido', models.ForeignKey(db_column='idpedido', on_delete=django.db.models.deletion.DO_NOTHING, to='pedido.pedido')),
                ('idproducto', models.ForeignKey(db_column='idproducto', on_delete=django.db.models.deletion.DO_NOTHING, to='producto.producto')),
            ],
            options={
                'db_table': 'pedidoxproducto',
            },
        ),
    ]
