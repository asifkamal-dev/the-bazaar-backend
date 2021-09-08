from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products',)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator',)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.TextField(default='https://thednetworks.com/wp-content/uploads/2012/01/picture_not_available_400-300.png')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Basket(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class SalesOrder(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    items = models.ManyToManyField(Basket)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username