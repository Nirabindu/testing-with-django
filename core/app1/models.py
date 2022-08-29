from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    regular_price = models.DecimalField(decimal_places=2,max_digits=5)
    
    
    