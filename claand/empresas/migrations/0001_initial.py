# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
                ('rfc', models.CharField(max_length=13, unique=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClienteTieneDireccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Cliente tiene direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('direccion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(to='empresas.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('link', models.URLField(null=True)),
                ('empresa', models.ForeignKey(to='empresas.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Redes Sociales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoRedSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Tipo Redes Sociales',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='redsocial',
            name='tipo_red_social',
            field=models.ForeignKey(null=True, to='empresas.TipoRedSocial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='municipio',
            field=models.ForeignKey(to='empresas.Municipio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientetienedireccion',
            name='direccion',
            field=models.ForeignKey(to='empresas.Direccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientetienedireccion',
            name='empresa',
            field=models.ForeignKey(to='empresas.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='direcciones',
            field=models.ManyToManyField(through='empresas.ClienteTieneDireccion', to='empresas.Direccion'),
            preserve_default=True,
        ),
    ]
