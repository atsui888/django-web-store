from django.urls import path
from shop.views.indexview import IndexView
from shop.views.productdetailsview import ProductDetailsView
from shop.views.shoppingcartview import ShoppingCartView

# the below are route patterns
urlpatterns = [
    path("category/<int:id>", IndexView.as_view(), name="category"),
    path("products/<int:id>", ProductDetailsView.as_view(), name="products"),
    path("shoppingcart", ShoppingCartView.as_view(), name="shoppingcart"),
    path("", IndexView.as_view(), name="index")
]