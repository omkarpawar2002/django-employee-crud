from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField(max_length=255)
    dept = models.CharField(max_length=100)
    sal = models.FloatField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField()