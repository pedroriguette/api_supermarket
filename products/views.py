from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project_supermarket.permissions import GlobalDefaultPermissionClass
from products.models import Product
from products.serializers import ProductSerializers

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers