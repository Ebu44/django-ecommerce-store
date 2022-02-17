from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .drf.views import AllProducts, ProductInventoryViewSet

router = routers.DefaultRouter()

router.register(r"api", viewset=AllProducts, basename="allproducts")

router.register(r"product", viewset=ProductInventoryViewSet, basename="products")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
