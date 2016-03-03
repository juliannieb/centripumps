# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20160302_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientetienedireccion',
            old_name='empresa',
            new_name='cliente',
        ),
    ]
