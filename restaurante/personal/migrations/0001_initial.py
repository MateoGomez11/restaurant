# Generated by Django 5.1.6 on 2025-02-13 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('idpersonal', models.AutoField(primary_key=True, serialize=False)),
                ('nombreper', models.CharField()),
                ('apellidoper', models.CharField()),
                ('puestoper', models.CharField()),
                ('estadoper', models.CharField()),
            ],
            options={
                'db_table': 'personal',
            },
        ),
    ]
