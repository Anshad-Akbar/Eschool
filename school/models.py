from django.db import models
from .models import *

# Create your models 
class Student_details(models.Model):
    name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    Email=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Conf_password=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    user_type=models.BooleanField(default=False)
