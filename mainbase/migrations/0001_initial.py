# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('formulation_name', models.CharField(max_length=200)),
                ('temperature_max', models.IntegerField()),
                ('emulsifier_to_solvent_ratio', models.CommaSeparatedIntegerField(max_length=10)),
                ('low_foam', models.BooleanField()),
                ('instructions', models.TextField()),
                ('development_notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ingredient_name', models.CharField(max_length=100)),
                ('percent_voc', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cleangredient', models.BooleanField()),
                ('estimate_cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('percent_by_mass', models.DecimalField(decimal_places=3, max_digits=4)),
                ('formulation', models.ForeignKey(to='mainbase.Formulation')),
                ('ingredient', models.ForeignKey(to='mainbase.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_types',
            field=models.ManyToManyField(to='mainbase.IngredientType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formulation',
            name='ingredients',
            field=models.ManyToManyField(through='mainbase.Recipe', to='mainbase.Ingredient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formulation',
            name='product_types',
            field=models.ManyToManyField(to='mainbase.ProductType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formulation',
            name='soils',
            field=models.ManyToManyField(to='mainbase.Soil'),
            preserve_default=True,
        ),
    ]
