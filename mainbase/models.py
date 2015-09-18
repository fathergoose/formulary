from django.db import models

# Create your models here.

class Soil(models.Model):
    soil_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.soil_name
    pass

class IngredientType(models.Model):
    ingredient_type_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.ingredient_type_name
    pass

class ProductType(models.Model):
    product_type_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.product_type_name
    pass

class Ingredient(models.Model):
    
    ingredient_name = models.CharField(max_length=100)
    ingredient_description = models.TextField(blank=True)
    estimate_cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="USD per pound")
    percent_voc = models.DecimalField(max_digits=3, decimal_places=2)
    cleangredient = models.NullBooleanField()
    ready_biodegradable = models.NullBooleanField()
    

    ingredient_types = models.ManyToManyField(IngredientType, blank=True)
    def __unicode__(self):
        return self.ingredient_name

class Formulation(models.Model):
    formulation_name = models.CharField(max_length=200)
    temperature_max = models.IntegerField()
    emulsifier_to_solvent_ratio = models.CommaSeparatedIntegerField(max_length=10)
    low_foam = models.BooleanField()
    instructions = models.TextField()
    development_notes = models.TextField()
    soils = models.ManyToManyField(Soil)
    product_types = models.ManyToManyField(ProductType)	
    ingredients = models.ManyToManyField(Ingredient, through='Recipe')
    def __unicode__(self):
        return self.formulation_name

class Recipe(models.Model):
    formulation = models.ForeignKey(Formulation)
    ingredient = models.ForeignKey(Ingredient)
    percent_by_mass = models.DecimalField(max_digits=4, decimal_places=3)
