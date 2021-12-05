from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from django.db import models
from cart.views import *
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


def product_detail(request, id):
	try:
		product = get_object_or_404(Product, id=id)
		category=Category.objects.get(id=id)
		cart_product_form = CartAddProductForm()

		context = {
	        'product': product,
	        'category':category,
	        'cart_product_form': cart_product_form,
	        }
	
	except Product.DoesNotExist:
		
		raise Http404 ("this product id does not exit")
	return render(request, 'products/product_detail.html', context)



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