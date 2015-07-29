# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0008_auto_20150429_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('costo', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], default=0)),
                ('tipo', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField(editable=False)),
                ('fecha_modificacion', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cotizado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('concepto', models.ForeignKey(to='cotizaciones.Concepto')),
                ('cotizacion', models.ForeignKey(to='cotizaciones.Cotizacion')),
            ],
            options={
                'verbose_name_plural': 'Cotizados',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='conceptos',
            field=models.ManyToManyField(through='cotizaciones.Cotizado', to='cotizaciones.Concepto'),
            preserve_default=True,
        ),
    ]
