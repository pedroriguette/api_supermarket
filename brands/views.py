from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project_supermarket.permissions import GlobalDefaultPermissionClass
from brands.models import Brand
from brands.serializers import BrandSerializers


class BrandListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers


class BrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
