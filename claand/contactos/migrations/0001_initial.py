# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oauth2client.django_orm
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('empresas', '0001_initial'),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Atiende',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Atienden',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('calificacion', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Calificaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('descripcion', models.TextField(max_length=1000)),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('clasificacion', models.IntegerField(default=1)),
                ('descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NumeroTelefonico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('numero', models.BigIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Número Telefónico',
                'verbose_name_plural': 'Números Telefónicos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pertenece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField()),
                ('area', models.ForeignKey(to='contactos.Area')),
            ],
            options={
                'verbose_name_plural': 'Pertenecen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pozo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_cliente', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('correo_electronico', models.EmailField(max_length=75, unique=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('calificacion', models.ForeignKey(null=True, to='contactos.Calificacion')),
                ('empresa', models.ManyToManyField(through='contactos.Pertenece', to='empresas.Cliente')),
                ('vendedor', models.ManyToManyField(through='contactos.Atiende', to='principal.Vendedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('descripcion', models.TextField(max_length=1000)),
                ('fecha', models.DateTimeField()),
                ('urgencia', models.IntegerField(default=1)),
                ('contacto', models.ForeignKey(to='contactos.Pozo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoNumeroTelefonico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pertenece',
            name='contacto',
            field=models.ForeignKey(to='contactos.Pozo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pertenece',
            name='empresa',
            field=models.ForeignKey(to='empresas.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='contacto',
            field=models.ForeignKey(blank=True, null=True, to='contactos.Pozo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, to='empresas.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='tipo_numero',
            field=models.ForeignKey(null=True, to='contactos.TipoNumeroTelefonico'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numerotelefonico',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, to='principal.Vendedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nota',
            name='contacto',
            field=models.ForeignKey(to='contactos.Pozo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='llamada',
            name='contacto',
            field=models.ForeignKey(to='contactos.Pozo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atiende',
            name='contacto',
            field=models.ForeignKey(to='contactos.Pozo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atiende',
            name='vendedor',
            field=models.ForeignKey(to='principal.Vendedor'),
            preserve_default=True,
        ),
    ]
