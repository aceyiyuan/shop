from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from django.db import models
from .models import Category, Product,Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView



def index(request):

    return render(request,'products/index.html')

#product_list

def product_list(request):

	products=Product.objects.order_by('id')[:10]
	categories=Category.objects.all()

	return render(request, 'products/product_list.html', {'products':products,'categories':'categories','sizes':'sizes'})


#product detail 
def product_detail(request,id):
	try:
		product=Product.objects.get(id=id)
		category=Category.objects.get(id=id)

	except Product.DoesNotExist:
		raise Http404 ("this product id does not exit")
	return render(request,'products/product_detail.html', {'product':product, 'category':'category', 'id':product.id,})



# cart List 
def cart_list(request):
	cart=Cart.objects.all()
	return render(request,'products/cart_list.html',{'cart':cart})
#add to cart

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
		data=Product.objects.filter(name__icontains=q).order_by('-id')
		return render(request,'products/search_result.html',{'data':data})


# Add to cart
def add_to_cart(request):
	# del request.session['cartdata']
	cart_p={}
	cart_p[str(request.GET['id'])]={
		'image':request.GET['image'],
		'title':request.GET['title'],
		'qty':request.GET['qty'],
		'price':request.GET['price'],
	}
	if 'cartdata' in request.session:
		if str(request.GET['id']) in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
			cart_data.update(cart_data)
			request.session['cartdata']=cart_data
		else:
			cart_data=request.session['cartdata']
			cart_data.update(cart_p)
			request.session['cartdata']=cart_data
	else:
		request.session['cartdata']=cart_p
	return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})



#404 page

def error_404_view(request, exception):
	return render(request, 'products/404.html')