from django.contrib import admin


# Register your models here.
from catalog.models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['title', "body"]
