from django.contrib import admin
from brands.models import Brand


@admin.register(Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo',)
