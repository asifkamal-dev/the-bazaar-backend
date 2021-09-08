from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Category, Product, SalesOrder, Basket

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedIdentityField(
        view_name='bazaar:category_detail',
        read_only=True
    )
    
    class Meta:
        model = Product
        fields = ('id','name','description','price','in_stock','category',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id','name',)