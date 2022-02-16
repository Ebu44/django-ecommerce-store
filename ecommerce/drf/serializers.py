from rest_framework import serializers
from ecommerce.inventory.models import Product


class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False