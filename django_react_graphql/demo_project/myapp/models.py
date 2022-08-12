from django.db import models


# Create your models here.

class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    middal_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
