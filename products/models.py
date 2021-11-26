from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):

		return self.name

	class Meta:
		#verbose_name = "Category"
		verbose_name_plural='Categories'

# food size

class Size(models.Model):
    title=models.CharField(max_length=50)

    class Meta:
    	verbose_name='Size'
    	verbose_name_plural='Sizes'

    def __str__(self):
        return self.title

#food type

class Portion(models.Model):
    title=models.CharField(max_length=50)

    class Meta:
    	verbose_name='Portion'
    	verbose_name_plural='Portions'
    def __str__(self):
        return self.title


# Product
class Product(models.Model):
	
	name = models.CharField(max_length=50, verbose_name="name")
	category=models.ForeignKey(Category, related_name='products',verbose_name="Category", on_delete=models.CASCADE, null=True)
	slug = models.SlugField(blank=True)
	size=models.ForeignKey(Size,on_delete=models.CASCADE)
	portion=models.ForeignKey(Portion,on_delete=models.CASCADE)
	description = models.TextField(blank=True,  verbose_name="description")
	price = models.DecimalField(max_digits=20, decimal_places=2, default=9.99, verbose_name="price")
	image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name="image")
	featured = models.BooleanField(default=False, verbose_name="featured")
	created = models.DateTimeField(auto_now_add=True, verbose_name="created")
	updated = models.DateTimeField(auto_now_add=True, verbose_name="updated")
	available=models.BooleanField(default=True, verbose_name="available")

	class Meta:
		verbose_name = "Product"
		verbose_name_plural='Products'

	def __str__(self):
		return self.name

	def image_tag(self):
		return mark_safe('<img src="%s" width="50" height="50" />)'% (self.image.url))



ONE='pending'
TWO='confirmed'
THREE='ontheway'
FOUR='cancelled'

Statuses  = [
		(ONE,'pending'),
		(TWO,'confirmed'),
		(THREE,'onetheway'),
		(FOUR,'cancelled'),

	]


#added to cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(choices=Statuses, max_length=20)
    ttl_amount = models.FloatField()
    added_date= models.DateTimeField(
            default=timezone.now)

    class Meta:
    	verbose_name_plural='Cart_list'


#single items in cart


class CartItems(models.Model):

	reference_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
	item=models.CharField(max_length=100)
	image=models.CharField(max_length=200)
	qty=models.IntegerField()
	price=models.FloatField()
	total=models.FloatField()

	class Meta:
		verbose_name_plural="Items"

	def image_tag(self):
		return mark_safe("<img src='/media/%s' width='50',height='50'/>" %(self.image))
