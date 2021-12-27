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
	description = models.TextField(blank=True,  verbose_name="description")
	featured = models.BooleanField(default=False, verbose_name="featured")
	created = models.DateTimeField(auto_now_add=True, verbose_name="created")
	updated = models.DateTimeField(auto_now_add=True, verbose_name="updated")
	available=models.BooleanField(default=True, verbose_name="available")
	has_attributes = models.BooleanField(default=False, verbose_name="attribute")
	image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name="image")
	price=models.DecimalField(max_digits=4, decimal_places=2, default=9.99, verbose_name="price")



	class Meta:
		verbose_name = "Product"
		verbose_name_plural='Products'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
  		return reverse('product:product_detail', args=[str(self.id)])

	def image_tag(self):
		return mark_safe('<img src="%s" width="50" height="50" />)'% (self.image.url))


class ProductAttribute(models.Model):
    
    product = models.ForeignKey('Product', related_name="product_attrs", on_delete=models.CASCADE)
    size = models.ForeignKey('Size', related_name="size", on_delete=models.CASCADE)
    portion = models.ForeignKey('Portion', related_name="portion", on_delete=models.CASCADE)
    code = models.CharField(max_length=6, verbose_name="code", default="piz002")
    price=models.DecimalField(max_digits=4, decimal_places=2, default=9.99, verbose_name="price")
    
    class Meta:
    	verbose_name='ProductAttribute'
    	verbose_name_plural='ProductAttributes'


    def __str__(self):
        return self.product.name












