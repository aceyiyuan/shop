from django.urls import path
from . import views
#from .views import product_list,  product_detail, cart_list,index, add_to_cart, error_404_view
from .models import *


app_name='product'

urlpatterns=[
	path('products/product_list', views.product_list, name='product_list'),
	path('products/search_result/', views.search_result, name='search_result'),
	path('products/<id>/', views.product_detail, name='product_detail'),
	#path('cart_list', views.cart_list, name='cart_list'),
	path('products/', views.index, name='index'),
	path('products/register',views.register,name='register'),

]

handler404='products.views.error_404_view'