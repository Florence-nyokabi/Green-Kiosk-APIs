from django.db import models
from inventory.models import Product

# Create your models here.
class Product_Cart(models.Model):
    product_name = models.CharField(max_length=32)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_quantity = models.IntegerField()
    product_image = models.ImageField()
    date_added = models.DateTimeField()
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = "product_cart"

    def total_price(self):
        return self.product_price * self.product_quantity

    def __str__(self):
        return self.product_name
