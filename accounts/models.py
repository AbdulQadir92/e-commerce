from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_or_email = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_or_email


class ShippingInformation(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state_or_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.address
