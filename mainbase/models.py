from django.db import models

# Create your models here.

class Formulation(models.Model):
    formulation_name = models.CharField(max_length=200)
    temperature_max = models.IntegerField()
    emulsifier_to_solvent_ratio = models.CommaSeparatedIntegerField(max_length=10)
    low_foam = models.BooleanField()
    development_notes = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='Recipe')
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
class Recipe(models.Model):
   
    
    
