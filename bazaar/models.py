from django.db import models
# from django.contrib.auth.models import User
## bringing in the new user model created from settings
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index= True)
    description = models.CharField(max_length=2550)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products',)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator', default=1)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.TextField(default='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Basket(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class SalesOrder(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    items = models.ManyToManyField(Basket)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user_name