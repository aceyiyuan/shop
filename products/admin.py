from django.contrib import admin

# Register your models here.
from .models import Product, Category,Size,Portion



class CategoryAdmin(admin.ModelAdmin):
	list_display=("id","name")
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display=("id","name","category","slug","size")
admin.site.register(Product, ProductAdmin)

admin.site.register(Size)
admin.site.register(Portion)