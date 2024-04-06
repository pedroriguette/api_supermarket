from rest_framework import serializers
from products.models import Product
from brands.models import Brand

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductRetrieveSerializer(ProductSerializers):

            class Meta(ProductSerializers.Meta):
                fields = ['name']
                