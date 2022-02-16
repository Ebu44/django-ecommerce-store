from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .drf.views import AllProducts

router = routers.DefaultRouter()
router.register(r"api", viewset=AllProducts, basename="allproducts")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
