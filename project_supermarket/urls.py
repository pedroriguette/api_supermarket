from django.contrib import admin
from django.urls import path, include
from products.views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from brands.views import BrandListCreateView, BrandRetrieveUpdateDestroyView
from categories.views import CategorieRetrieveUpdateDestroyView, CategoryListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),

    path('products/', ProductListCreateView.as_view(), name='product-list-detail-view'),
    path('products/<int:pk>/', 
         ProductRetrieveUpdateDestroyView.as_view(), 
         name='product-retrieve-update-detroy-view'
         ),

    path('brands/', BrandListCreateView.as_view(), name='brand-list-detail-view'),
    path('brands/<int:pk>/', 
         BrandRetrieveUpdateDestroyView.as_view(), 
         name='brand-retrieve-update-detroy-view'
         ),

     path('categories/', CategoryListCreateView.as_view(), name='categorie-list-create-view'),
     path('categories/<int:pk>/', 
          CategorieRetrieveUpdateDestroyView.as_view(), 
          name='categorie-detail-update-destroy-view'
          ),

]
