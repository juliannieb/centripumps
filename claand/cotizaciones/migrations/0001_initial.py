# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('costo', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('tipo', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('monto', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('descripcion', models.TextField()),
                ('is_pendiente', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
                'verbose_name': 'Cotización',
                'verbose_name_plural': 'Cotizaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cotizado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
                ('concepto', models.ForeignKey(to='cotizaciones.Concepto')),
                ('cotizacion', models.ForeignKey(to='cotizaciones.Cotizacion')),
            ],
            options={
                'verbose_name_plural': 'Cotizados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
                ('monto', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('monto_total', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('monto_acumulado', models.FloatField(default=0)),
                ('is_completada', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('cotizacion', models.OneToOneField(to='cotizaciones.Cotizacion')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='venta',
            field=models.ForeignKey(to='cotizaciones.Venta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='conceptos',
            field=models.ManyToManyField(through='cotizaciones.Cotizado', to='cotizaciones.Concepto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='contacto',
            field=models.ForeignKey(to='contactos.Pozo'),
            preserve_default=True,
        ),
    ]
