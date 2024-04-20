from django.db import models
from brands.models import Brand
from categories.models import Categorie


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='brand',
        blank=True,
        null=True
    )
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.PROTECT,
        related_name='categorie',
        blank=True,
        null=True
    )
    value = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
