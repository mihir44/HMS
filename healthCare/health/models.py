from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    phone = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()


    def __str__(self):
        return self.name
