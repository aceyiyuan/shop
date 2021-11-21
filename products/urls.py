from django.urls import path
from . import views
from .models import *
app_name='product'

urlpatterns=[
	path('products/product_list', views.product_list, name='product_list'),
	#path('products/search', views.search, name='search'),
	path('products/<id>/', views.product_detail, name='product_detail'),
	path('cart_list', views.cart_list, name='cart_list'),
	path('products/', views.index, name='index'),

]

handler404='products.views.error_404_view'