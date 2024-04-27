from rest_framework import serializers
from brands.models import Brand


class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class BrandRetrieveSerializer(serializers.Serializer):
    brand = serializers.CharField()
    value_in_stock = serializers.FloatField()
    total_products = serializers.IntegerField()
