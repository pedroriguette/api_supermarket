from django.urls import path
from brands.views import BrandListCreateView, BrandRetrieveUpdateDestroyView


urlpatterns = [
    path('brands/', BrandListCreateView.as_view(), name='brand_list_create_view'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='brand_retrieve_update_detroy_view',)
]
