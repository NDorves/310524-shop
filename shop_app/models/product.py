from django.db import models
from .category import Category
from .supplier import Supplier



class Product(models.Model):
   name = models.CharField(max_length=100)
   category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
   supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='products')
   price = models.DecimalField(max_digits=10, decimal_places=2)
   quantity = models.PositiveSmallIntegerField()
   article = models.CharField(max_length=100, unique=True, help_text='Unique string product id',
                              db_index=True)
   available = models.BooleanField(default=True)


   def __str__(self):
       return self.name


   class Meta:
       ordering = ['category', 'quantity']