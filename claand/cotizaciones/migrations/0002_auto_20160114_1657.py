# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brinda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('precio', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CotizacionUtilizaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('cotizacion', models.ForeignKey(to='cotizaciones.Cotizacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CotizacionUtilizaServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('cotizacion', models.ForeignKey(to='cotizaciones.Cotizacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('lugar', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('precio', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], default=0.0)),
                ('producto', models.ForeignKey(to='cotizaciones.Producto')),
                ('proveedor', models.ForeignKey(to='cotizaciones.Proveedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cotizado',
            name='concepto',
        ),
        migrations.RemoveField(
            model_name='cotizado',
            name='cotizacion',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='productos',
            field=models.ManyToManyField(through='cotizaciones.Vende', to='cotizaciones.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='servicios',
            field=models.ManyToManyField(through='cotizaciones.Brinda', to='cotizaciones.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cotizacionutilizaservicio',
            name='servicio',
            field=models.ForeignKey(to='cotizaciones.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cotizacionutilizaproducto',
            name='producto',
            field=models.ForeignKey(to='cotizaciones.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brinda',
            name='proveedor',
            field=models.ForeignKey(to='cotizaciones.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brinda',
            name='servicio',
            field=models.ForeignKey(to='cotizaciones.Servicio'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='conceptos',
        ),
        migrations.DeleteModel(
            name='Cotizado',
        ),
        migrations.DeleteModel(
            name='Concepto',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='productos',
            field=models.ManyToManyField(through='cotizaciones.CotizacionUtilizaProducto', to='cotizaciones.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='servicios',
            field=models.ManyToManyField(through='cotizaciones.CotizacionUtilizaServicio', to='cotizaciones.Servicio'),
            preserve_default=True,
        ),
    ]
