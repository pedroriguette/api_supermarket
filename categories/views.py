from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from project_supermarket.permissions import GlobalDefaultPermissionClass
from categories.models import Categorie
from categories.serializers import CategorieSerializer
from products.models import Product
from products.serializers import ProductSerializers


class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

    #reescrever o metodo get da classe
    def get(self, request, pk): 
        #busca o objeto de acordo com a pk enviado na requisição
        categorie = self.get_object() 
        #filtrar pelo id da lista de produto que está conectada ao id da categoria
        products = Product.objects.filter(categorie=categorie) 

        categorie_serializer = self.get_serializer(categorie)
        # Definindo um serializador personalizado apenas para esta view
        class ProductRetrieveSerializer(ProductSerializers):
            class Meta(ProductSerializers.Meta):
                fields = ['name']

        products_serializer = ProductRetrieveSerializer(products, many=True)

        data = {
            'categorie': categorie_serializer.data,
            'products': products_serializer.data}

        return Response(data, status=status.HTTP_200_OK)
    

