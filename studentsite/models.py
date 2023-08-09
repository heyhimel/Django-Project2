from django.db import models

# Create your models here.


class studentdetails(models.Model):
    roll = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    regno = models.CharField(max_length=5)
    semister = models.CharField(max_length=20)
    courses = models.CharField(max_length=500)
