# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainbase', '0003_auto_20150918_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='cleangredient',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ready_biodegradable',
            field=models.NullBooleanField(),
        ),
    ]
