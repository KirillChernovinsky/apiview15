from django.contrib import admin

from .models import Meal, Ingredients

# Register your models here.

admin.site.register(Meal)
admin.site.register(Ingredients)