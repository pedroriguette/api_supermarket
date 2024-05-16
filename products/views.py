from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from project_supermarket.permissions import GlobalDefaultPermissionClass
from products.models import Product
from products.serializers import ProductSerializers


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        "name",
        "brand",
        "categorie",
    ]
    search_fields = [
        "name",
        "brand__name",
    ]
    ordering = ["id"]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
