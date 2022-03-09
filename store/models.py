from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='categoryImages', null=True)

    def __str__(self):
        return self.category


class Subcategories(models.Model):
    subcategory = models.CharField(max_length=50)
    subcategory_image = models.ImageField(upload_to='subcategoryImages', null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory


class MoreCategories(models.Model):
    more_category = models.CharField(max_length=50)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.more_category


class SliderImages(models.Model):
    slider_image = models.ImageField(upload_to='sliderImages')


class Brand(models.Model):
    brand = models.CharField(max_length=50)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.brand


class Product(models.Model):
    primary_image = models.ImageField(upload_to='images', null=True)
    secondary_image1 = models.ImageField(upload_to='secondaryImages', null=True, blank=True)
    secondary_image2 = models.ImageField(upload_to='secondaryImages', null=True, blank=True)
    secondary_image3 = models.ImageField(upload_to='secondaryImages', null=True, blank=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    rating = models.IntegerField(default=0)
    shipping = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    digital = models.BooleanField(default=False)
    home_delivery = models.CharField(max_length=50, null=True)
    cash_on_delivery = models.BooleanField(default=False, null=True)
    return_service = models.CharField(max_length=100, null=True)
    change_of_mind = models.BooleanField(default=False, null=True)
    brand_warranty = models.CharField(max_length=100, null=True)
    more_category = models.ForeignKey(MoreCategories, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    product_id = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    # def __str__(self):
    #     return self.product_id


class WishList(models.Model):
    product_id = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
