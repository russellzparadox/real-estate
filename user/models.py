from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(region='IR')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
