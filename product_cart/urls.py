from django.urls import path
from .views import upload_products, edit_cart_details, display_cart_products, clear_product_cart

urlpatterns = [
    path("upload_product/<int:id>/",upload_products, name="product_cart_list"),
    path("edit_product_cart/", edit_cart_details, name="edit_cart"),
    path("view_product_cart/<int:id>/", display_cart_products, name="display_cart_products"),
    path("clear_from_cart/", clear_product_cart, name="clear_product_cart"),
]