from django.contrib import admin
from .models import Product, Staff, Contact, ProductStock

# Register your models here.
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Contact)
admin.site.register(ProductStock)