from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)




class Product(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    stock = models.CharField(max_length=100, null=True, blank=True)
    des = models.TextField(max_length=100, null=True, blank=True) 
    price = models.IntegerField(null=True, blank= True)
    image = models.ImageField(upload_to='product_images')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE) 


class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity= models.IntegerField(default=1)


    def __str__(self):
        return self.name

