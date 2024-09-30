from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='user/')