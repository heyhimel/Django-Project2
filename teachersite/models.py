from django.db import models

# Create your models here.


class register(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    username=models.CharField(max_length=20)