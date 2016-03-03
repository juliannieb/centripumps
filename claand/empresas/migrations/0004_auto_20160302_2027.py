# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20160302_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono1',
            field=models.CharField(max_length=10, default='', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono2',
            field=models.CharField(max_length=10, default='', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono3',
            field=models.CharField(max_length=10, default='', null=True),
            preserve_default=True,
        ),
    ]
