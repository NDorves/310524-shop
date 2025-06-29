from django.contrib import admin
from .models import Category, Supplier, Product, Customer, Address, Order, OrderItem, ProductDetail

# Register your models here.

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductDetail)


