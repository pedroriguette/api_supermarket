from rest_framework import generics, status, response
from rest_framework.permissions import IsAuthenticated
from project_supermarket.permissions import GlobalDefaultPermissionClass
from categories.models import Categorie
from categories.serializers import CategorieSerializer, CategorieRetrieveView
from products.models import Product


class CategorieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class CategorieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Categorie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorieRetrieveView
        return CategorieSerializer

    def get(self, request, pk):
        categorie = self.get_object()
        products = Product.objects.filter(categorie=categorie)
        data = {
            'categorie': categorie.name,
            'products': products.values(),
            'total_products': products.values().count()
        }

        serializer = CategorieRetrieveView(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )
