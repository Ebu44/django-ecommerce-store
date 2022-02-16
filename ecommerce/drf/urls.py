from django.urls.conf import path
from .views import AllProducts

urlpatterns = [path("", AllProducts.as_view())]
