from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class AdminProduct(models.Model):
    pro_name = models.CharField(max_length=32)
    pro_description = models.TextField()
    pro_image = models.TextField()
    pro_code = models.CharField(max_length=32)
    pro_range = models.CharField(max_length=32)
    pro_features = models.TextField()
    pro_price = models.IntegerField()
    pro_price_per_user = models.IntegerField()
    pro_price_plumber = models.IntegerField()
    pro_price_prime = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")


    def __str__(self):
        return self.pro_code
    
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    contact = models.CharField(max_length=12, blank=True, null=True)
    
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")
    