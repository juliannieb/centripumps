# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='contacto',
            new_name='Pozo',
        ),
        migrations.RenameField(
            model_name='pertenece',
            old_name='empresa',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='pertenece',
            old_name='contacto',
            new_name='pozo',
        ),
        migrations.RenameField(
            model_name='pozo',
            old_name='empresa',
            new_name='cliente',
        ),
        migrations.RemoveField(
            model_name='pertenece',
            name='area',
        ),
        migrations.RemoveField(
            model_name='pozo',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='pozo',
            name='calificacion',
        ),
        migrations.RemoveField(
            model_name='pozo',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='pozo',
            name='is_cliente',
        ),
        migrations.RemoveField(
            model_name='pozo',
            name='vendedor',
        ),
        migrations.AlterField(
            model_name='pozo',
            name='nombre',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
