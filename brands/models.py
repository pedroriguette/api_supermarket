from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
