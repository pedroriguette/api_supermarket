from django.urls import path
from categories.views import CategoryListCreateView, CategorieRetrieveUpdateDestroyView


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categorie_list_create_view'),
    path('categories/<int:pk>/', CategorieRetrieveUpdateDestroyView.as_view(), name='categorie_detail_update_destroy_view'),
]
