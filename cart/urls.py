from django.urls import path
from . import views


app_name='cart'

urlpatterns=[
	path('cart/cart_summary', views.cart_summary, name='cart_summary'),
	path('cart/cart_remove/product.id',views.cart_delete, name='cart_delete'),
	path('cart/cart_add/product.id',views.cart_add, name='cart_add'),
	path('cart/cart_update',views.cart_update, name='cart_update'),
]

#handler404='cart.views.error_404_view'



