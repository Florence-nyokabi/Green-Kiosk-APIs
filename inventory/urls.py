# urls.py
from django.urls import path
from .views import product_upload_view, product_list, product_details

urlpatterns = [
    path("products/upload/", product_upload_view, name="product_upload_view"),
    path("products/list/", product_list, name="product_list_view"),
    path("products/<int:id>/", product_details, name="product_detail_view"),
]
