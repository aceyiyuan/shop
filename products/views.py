from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from django.db import models
from .models import Category, Product
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404,redirect
from django.views.generic.list import ListView
from cart.forms import CartAddProductForm
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib import messages

from itertools import chain
from django.db.models import Q
#import django_filters





def index(request):

    return render(request,'products/index.html')

#product_list

#cart_product_form = CartAddProductForm()

def product_list(request):

	products=Product.objects.order_by('id')[:10]
	categories=Category.objects.all()


	return render(request, 'products/product_list.html',  {'products':products,'categories':categories})


#product detail 
def product_detail(request,id):
	try:
		product=Product.objects.get(id=id)
		category=Category.objects.get(id=id)

	except Product.DoesNotExist:
		raise Http404 ("this product id does not exit")
	return render(request,'products/product_detail.html', {'product':product, 'category':category, 'id':product.id,})


"""
# cart List 
def cart_list(request):
	cart=Cart.objects.all()
	return render(request,'products/cart_list.html',{'cart':cart})
#add to cart
"""
"""
@login_required
def add_to_cart(request,Product.id):
    item = get_object_or_404(Product, id=product.id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    order,created = Product.objects.get_or_create(item=product,cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, "Cart updated!")
    return redirect('cart')

"""
# Search



# Search







def search_result(request):

	q=request.GET['q']
	if not q:
		return HttpResponse("please input some texts")
	else:
		product_result=Product.objects.filter( Q(name__icontains=q)|Q(code__icontains=q)).order_by('name', 'price') #filter product results by search word
		category_result=Category.objects.filter(name__icontains=q).order_by('name') #filter category results by search word

		data = chain(product_result, category_result) #from itertools import chain
		return render(request,'products/search_result.html',{'data':data})


def register(request):
	if request.method=='POST':
		form=NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			pwd=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=pwd)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/products/')
		messages.error(request, "Unsuccessful registration")
	form=NewUserForm
	return render(request, 'products/register.html',{'form':form})



def error_404_view(request, exception):
	return render(request, 'products/404.html')