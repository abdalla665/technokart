from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    price_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    images          = models.ImageField(upload_to='photos/products')
    is_available    = models.BooleanField(default=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name