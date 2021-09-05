from django.contrib import admin
from .models import Category, Product, SalesOrder, OrderStaging
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','created_by','name','slug','price','description','image','in_stock','created','updated','is_active']
    list_filter = ['in_stock','is_active']
    list_editable = ['price','in_stock','is_active']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(SalesOrder)
admin.site.register(OrderStaging)