from django.db import models

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    house = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.house}, {self.city}, {self.country}"