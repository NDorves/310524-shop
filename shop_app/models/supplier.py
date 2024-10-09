from django.db import models



class Supplier(models.Model):
   name = models.CharField(max_length=100, unique=True)
   contact_email = models.EmailField(unique=True)
   phone_number = models.CharField(max_length=20, unique=True)


   def __str__(self):
       return self.name