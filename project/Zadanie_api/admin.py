from django.contrib import admin

from .models import Tovar, Category, Maker

# Register your models here.

admin.site.register(Tovar),
admin.site.register(Category),
admin.site.register(Maker),