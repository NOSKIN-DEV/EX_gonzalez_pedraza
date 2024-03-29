# Generated by Django 5.0.1 on 2024-01-30 02:25

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.BigIntegerField()),
                ('fechaCompra', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='detalle_boleta',
            fields=[
                ('id_detalle_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.productos')),
                ('id_boleta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carrito.boleta')),
            ],
        ),
    ]
