from django.contrib import admin

# Register your models here.
from .models import Formulation

admin.site.register(Formulation)

from .models import Ingredient

admin.site.register(Ingredient)

from .models import Soil

admin.site.register(Soil)

from .models import ProductType

admin.site.register(ProductType)

from .models import IngredientType

admin.site.register(IngredientType)

from .models import Recipe

admin.site.register(Recipe)