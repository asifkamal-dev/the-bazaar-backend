from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name= 'bazaar'

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('basket/', views.BasketList.as_view(), name='basket_list'),
    path('basket/<int:pk>', views.BasketDetail.as_view(), name='basket_detail'),
]
