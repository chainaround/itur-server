from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    instock = models.DecimalField(default=1, max_digits=10, decimal_places=2)
    sold = models.DecimalField(default=1, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + '(instock: {} sold {})'.format(self.instock, self.sold)

class Staff(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    detail = models.TextField(null=True, blank=True)
    mail = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title