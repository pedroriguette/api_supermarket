from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from project_supermarket.permissions import GlobalDefaultPermissionClass
from categories.models import Categorie
from categories.serializers import CategorieSerializer
from products.models import Product
from products.serializers import ProductSerializers, ProductRetrieveSerializer


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
        # Convertendo os nomes dos produtos para maiúsculas antes de serializá-los
        products_data = [{'name':product.name.capitalize()} for product in products]
        products_serializer = ProductRetrieveSerializer(data=products_data, many=True)
        products_serializer.is_valid()
        data = {
            'categorie': categorie_serializer.data,
            'products': products_serializer.data}
        return Response(data, status=status.HTTP_200_OK)
