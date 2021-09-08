from django.contrib import admin
from .models import Category, Product, SalesOrder, Basket
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','created_by','name','price','description','image','in_stock','created','updated','is_active']
    list_filter = ['in_stock','is_active']
    list_editable = ['price','in_stock','is_active']


admin.site.register(SalesOrder)
admin.site.register(Basket)