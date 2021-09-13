from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

app_name= 'bazaar'

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('basket/', views.BasketList.as_view(), name='basket_list'),
    path('basket/<int:pk>', views.BasketDetail.as_view(), name='basket_detail'),
    path('orders/', views.SalesOrderList.as_view(), name='SalesOrder_list'),
    path('order/<int:pk>', views.SalesOrderDetail.as_view(), name='SalesOrder_detail'),
]
