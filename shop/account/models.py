from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    is_verified = models.BooleanField(default=False)

class Address(models.Model):

    class AddressType(models.TextChoices):
        BILLING =
    descrition = models.TextField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField()