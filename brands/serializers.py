from rest_framework import serializers
from brands.models import Brand

class BrandSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'