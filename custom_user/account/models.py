from django.db import models
from django.contrib.auth.models import AbstractUser
from .manage import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username= None
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=30)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
    objects= UserManager()

    def __str__(self):
        return self.email
