from django.contrib import admin

# Register your models here.
from shop.models import Product
from shop.models import Category
from shop.models import City

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(City)


