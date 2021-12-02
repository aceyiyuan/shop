from django.urls import path
from . import views


app_name='cart'

urlpatterns=[


	path('cart/cart_add/product.id',views.cart_add, name='cart_add'),

]

#handler404='cart.views.error_404_view'





