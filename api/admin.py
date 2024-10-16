from django.contrib import admin
from .models import Brewery

# Register your models here.

class BreweryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brewery, BreweryAdmin)