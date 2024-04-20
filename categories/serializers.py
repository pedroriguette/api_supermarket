from rest_framework import serializers
from categories.models import Categorie


class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = '__all__'


class CategorieRetrieveView(serializers.Serializer):
    categorie = serializers.CharField()
    products = serializers.ListField()
    total_products = serializers.IntegerField()
