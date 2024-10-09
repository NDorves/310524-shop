from django.db import models
from .product import Product



class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Details for {self.product.name}"