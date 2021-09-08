from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Category, Product, Basket, SalesOrder
from .serializers import ProductSerializer, CategorySerializer, BasketSerializer, SalesOrderSerializer

# Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Basket/Staging
class BasketList(generics.ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

# SalesOrder
class SalesOrderList(generics.ListCreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

class SalesOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
