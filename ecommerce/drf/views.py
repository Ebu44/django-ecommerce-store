from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from ecommerce.inventory.models import Product, ProductInventory
from .serializers import AllProductsSerializer, ProductInventorySerializer


class AllProducts(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)[:10]
        serializer = AllProductsSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
