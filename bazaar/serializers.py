from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, SalesOrder, Basket



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.HyperlinkedRelatedField(
        view_name='bazaar:category_detail',
        queryset = Category.objects.all()
        # read_only=True
    )
    # category_id = serializers.SlugRelatedField(
    #     view_name='bazaar:category_detail',
    #     queryset = Category.objects.all()
    #     # read_only=True
    # )
    created_by = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
    )


    class Meta:
        model = Product
        fields = ('id','name','description','created_by','price','in_stock','category_id',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        view_name='bazaar:product_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('id','name','products')
    
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
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
    )

    class Meta:
        model = SalesOrder
        fields = ('user','items','start_date','ordered_date','ordered',)

