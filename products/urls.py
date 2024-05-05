from django.urls import path
from products.views import ProductListCreateView, ProductRetrieveUpdateDestroyView


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product_list_create_view'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product_retrieve_update_detroy_view'),
]
