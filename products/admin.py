from django.contrib import admin
from .models import Products, ProductTypes, ProductImages

# Register your models here.
admin.site.register(ProductTypes)
admin.site.register(Products)
admin.site.register(ProductImages)