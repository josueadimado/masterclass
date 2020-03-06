from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import json

# Create your models here.
class CustomUser(AbstractUser):
    # additional fields
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30, null=True)
    professionalstatus = models.CharField(max_length=30, null=True)
    institution = models.CharField(max_length=30, null=True)
    interest = models.CharField(max_length=30, null=True)
    expectation = models.CharField(max_length=2000, null=True)


    def __str__(self):
        return self.username
