from typing import Any
from django.db import models
from user.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=30)
    image = models.ImageField(upload_to='product/')
    batafsil = models.TextField(null=True)
    narxi = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User)

    class Meta:
        ordering = ('name',)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Savat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

class Like(models.Model):
    user = models.ManyToManyField(User)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='likes')
