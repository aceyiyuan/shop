from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.utils import timezone


# food size

class Size(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
    	verbose_name='Size'
    	verbose_name_plural='Sizes'

    def __str__(self):
        return self.name

#food type

class Portion(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
    	verbose_name='Portion'
    	verbose_name_plural='Portions'
    def __str__(self):
        return self.name



class Category(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):

		return self.name

	class Meta:
		#verbose_name = "Category"
		verbose_name_plural='Categories'



# Product
class Product(models.Model):
	
	name = models.CharField(max_length=50, verbose_name="name")
	category=models.ForeignKey(Category, related_name='products',verbose_name="Category", on_delete=models.CASCADE, null=True)
	slug = models.SlugField(blank=True)
	code = models.CharField(max_length=6, verbose_name="code", default="piz002")
	size=models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name="size")
	portion=models.ForeignKey(Portion,on_delete=models.CASCADE,verbose_name="portion")
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


