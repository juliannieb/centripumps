# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0002_auto_20160114_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='brinda',
            name='fecha_creacion',
            field=models.DateField(editable=False, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brinda',
            name='fecha_modificacion',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vende',
            name='fecha_creacion',
            field=models.DateField(editable=False, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vende',
            name='fecha_modificacion',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
