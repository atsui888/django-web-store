from django.urls import path
from shop.views.indexview import IndexView
from shop.views.productdetailsview import ProductDetailsView
from shop.views.shoppingcartview import ShoppingCartView
from shop.views.deliveryaddressview import DeliveryAddressView
from shop.views.orderconfirmview import OrderConfirmView

# the below are route patterns
urlpatterns = [
    path("category/<int:id>", IndexView.as_view(), name="category"),
    path("products/<int:id>", ProductDetailsView.as_view(), name="products"),
    path("shoppingcart", ShoppingCartView.as_view(), name="shoppingcart"),
    path("deliveryaddress", DeliveryAddressView.as_view(), name="deliveryaddress"),
    path("orderconfirm", OrderConfirmView.as_view(), name="orderconfirm"),
    path("", IndexView.as_view(), name="index")
]
