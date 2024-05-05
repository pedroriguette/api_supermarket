from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):

    def get(self, request, format=None):
        return Response({
            'Authentication': {
                'token_obtain_pair': reverse('token_obtain_pair', request=request, format=format),
                'token_refresh': reverse('token_refresh', request=request, format=format),
                'token_verify': reverse('token_verify', request=request, format=format),
            },
            'brands': {
                'brand_list_create_view': reverse('brand_list_create_view', request=request, format=format),
                'brand_retrieve_update_detroy_view': reverse('brand_retrieve_update_detroy_view', kwargs={'pk': 1}, request=request, format=format),
            },
            'products': {
                'product_list_create_view': reverse('product_list_create_view', request=request, format=format),
                'product_retrieve_update_detroy_view': reverse('product_retrieve_update_detroy_view', kwargs={'pk': 1}, request=request, format=format),
            },
            'categories': {
                'categorie_list_create_view': reverse('categorie_list_create_view', request=request, format=format),
                'categorie_detail_update_destroy_view': reverse('categorie_detail_update_destroy_view', kwargs={'pk': 1}, request=request, format=format),
            }
        })
