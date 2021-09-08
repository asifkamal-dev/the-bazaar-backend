from django.db.models import query
from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Category, Product, SalesOrder, Basket
from bazaar import models

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
    
class BasketSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='bazaar:product_detail',
        read_only=True
    )

    class Meta:
        model = Basket
        fields = ('ordered','product','quantity',)

class SalesOrderSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        queryset = Basket.objects.all(),
        many=True
    )
    

    class Meta:
        model = SalesOrder
        fields = ('items','start_date','ordered_date','ordered',)
        # fields = ('start_date','ordered_date','ordered',)