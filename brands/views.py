from django.db.models import Sum
from rest_framework import generics, status, response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from project_supermarket.permissions import GlobalDefaultPermissionClass
from brands.models import Brand
from brands.serializers import BrandSerializers, BrandRetrieveSerializer
from products.models import Product


class BrandListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

    filter_backends = [SearchFilter]
    search_fields = ["name"]

    ordering = ['id']


class BrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Brand.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BrandRetrieveSerializer
        return BrandSerializers

    def get(self, request, pk):
        brand_id = self.get_object()
        products_value = Product.objects.filter(brand_id=brand_id)
        value_in_stock = products_value.aggregate(total=Sum('value'))['total'] or 0.0

        data = {
            'brand': brand_id.name,
            'value_in_stock': value_in_stock,
            'total_products': products_value.count()
        }

        serializer = BrandRetrieveSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
