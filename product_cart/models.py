from django.db import models
from inventory.models import Product

# Create your models here.
class Product_Cart(models.Model):
    product_name = models.CharField(max_length=32)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image =models.ImageField()
    date_added = models.DateTimeField()
    products = models.ManyToManyField(Product) 

class Meta:
        verbose_name_plural = "product_cart"
