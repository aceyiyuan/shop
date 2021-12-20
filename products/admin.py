from django.contrib import admin

# Register your models here.
from .models import Product, Category,Size,Portion,ProductAttribute



class CategoryAdmin(admin.ModelAdmin):
	list_display=("id","name")
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display=("id","name","category","slug")


# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','code','size','portion')

admin.site.register(ProductAttribute,ProductAttributeAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Size)
admin.site.register(Portion)
