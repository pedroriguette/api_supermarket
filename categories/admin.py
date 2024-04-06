from django.contrib import admin
from categories.models import Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    