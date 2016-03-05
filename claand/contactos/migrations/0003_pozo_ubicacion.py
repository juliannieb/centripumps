# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0002_auto_20160302_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='pozo',
            name='ubicacion',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
