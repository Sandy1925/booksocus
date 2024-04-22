from django.db import models

# Create your models here.
"""
Customer Model
Author: Santhosh Kumar
 Date Created: 10/01/24
 Date Modified:
"""
class Customer(models.Model):
    code=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)

