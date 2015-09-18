# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainbase', '0002_auto_20150918_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ready_biodegradable',
            field=models.BooleanField(default=datetime.datetime(2015, 9, 18, 2, 32, 38, 599302, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='estimate_cost',
            field=models.DecimalField(help_text=b'USD per pound', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_types',
            field=models.ManyToManyField(to='mainbase.IngredientType', blank=True),
        ),
    ]
