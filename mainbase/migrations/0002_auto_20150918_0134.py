# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainbase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredienttype',
            name='ingredient_type_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 18, 1, 34, 15, 59305, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttype',
            name='product_type_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 18, 1, 34, 28, 19348, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soil',
            name='soil_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 18, 1, 34, 37, 715352, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
