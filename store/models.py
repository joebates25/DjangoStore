from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, default="")
    parent = models.ForeignKey("Category", null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Listing(models.Model):
    name = models.CharField(max_length=200, default="")
    category = models.ForeignKey(Category, null=True, blank=True)
    products = models.ManyToManyField("Product", blank=True, through="ProductListing")
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return str(self.name)



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default="")
    price = models.IntegerField(default=1)
    availableQuantity = models.IntegerField(default=1)
    picture = models.ImageField(null=True, blank=True)
    date_left = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def removeQuantity(self, q):
        self.availableQuantity -= 1



class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    date_left = models.DateField(null=True, blank=True)
    def total_price(self):
        return self.product.price * self.quantity

'''
    Test Stuff Here
'''
class ProductListing(models.Model):
    listing = models.ForeignKey(Listing)
    product = models.ForeignKey(Product)
    date_joined = models.DateField(null=True, blank=True)
    date_left = models.DateField(null=True, blank=True)


class ProductListingInline(admin.TabularInline):
    model = ProductListing
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductListingInline,)

class ListingAdmin(admin.ModelAdmin):
    inlines = (ProductListingInline,)


