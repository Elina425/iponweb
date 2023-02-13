from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="cunstomer/", blank=True, null=True)
class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/')
    registered_at = models.DateTimeField(default=timezone.now)
    slug =models.SlugField(max_length=100)
class Category(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True,related_name='child', on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Store(models.Model):
    name = models.TextField(max_length=100)
    owner =models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug =models.SlugField(max_length=100)


class Item(models.Model):
    category = models.ForeignKey(Category,related_name='item', on_delete=models.CASCADE)
    name = models.TextField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_creator')
    image = models.ImageField(upload_to='images/');
    slug = models.SlugField(max_length=100)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    info = models.TextField(max_length=10000)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
class Mybug(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.FloatField()
    slug =models.SlugField(max_length=100)

class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField()
    slug =models.SlugField(max_length=100)
