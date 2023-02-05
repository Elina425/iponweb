from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)
class Seller(models.Model):
    name = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
class Category(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True         ,related_name='child', on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
