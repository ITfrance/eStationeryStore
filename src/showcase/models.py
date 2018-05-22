from django.db import models
from django.utils.html import mark_safe
import uuid

class Item(models.Model):
    
    product=models.CharField(max_length=200,verbose_name='Producto')
    
    idProvider=models.CharField(max_length=36,verbose_name='ID UNICO',primary_key=True,unique=True)
    stock=models.PositiveSmallIntegerField(default=0,verbose_name='Stock Actual')
    minimumStock=models.PositiveSmallIntegerField(default=0,verbose_name='Stock Minimo')
    photo=models.ImageField(upload_to='items',default='items/noImage.png')
    description=models.CharField(max_length=200,verbose_name='Descripción',default='')    
    last_modified=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product
    
    def image_tag(self):
        return mark_safe('<img src=%s width="100">'% self.photo.url) 
    
    def low_stock(self):
        return self.stock < self.minimumStock
    
    def stock_ok(self):
        return self.stock >= self.minimumStock
    
    image_tag.short_description = 'Foto'
    
class User(models.Model):
    """ """
    id_AD = models.CharField(max_length = 10, verbose_name = 'User ID', primary_key = True, unique = True)
    mail = models.EmailField(max_length = 50, verbose_name = 'Email', default = '', unique = True)
    name = models.CharField(max_length = 50, verbose_name = 'Name', default = '')
    last_name = models.CharField(max_length = 50, verbose_name = 'Last Name', default = '')
    
    def __str__(self):
        return self.last_name + ", " + self.name

class ItemQuantityPair(models.Model):
    """ """
    item = models.ForeignKey(Item,null=True,on_delete=models.SET_NULL,verbose_name='Item', default = None)
    quantity = models.PositiveSmallIntegerField(default=0,verbose_name='Quantity')
    
    def __str__(self):
      return self.item.product + ", Qty. " + str(self.quantity)
    
class Purchase(models.Model):
    """ """
    number=models.CharField(max_length=36,verbose_name='Number',primary_key=True,unique=True, default = '')
    date=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    items=models.ManyToManyField(ItemQuantityPair,verbose_name='Products', default = None)    
    comments=models.CharField(max_length=400,verbose_name='Comments', blank=True, default = '')
    total_amount=models.DecimalField(max_digits=6,decimal_places=2, verbose_name='Invoice Total (ARS)', default = 0)    
    
    def __str__(self):
      return self.number
    
class Delivery(models.Model):
    """ """
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name='User', default = None)
    date=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    items=models.ManyToManyField(ItemQuantityPair,verbose_name='Products', default = None)
    comments=models.CharField(max_length=400,verbose_name='Comments', default = '')
    
    def __str__(self):
      return self.id