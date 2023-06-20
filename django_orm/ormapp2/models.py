from django.db import models

# Create your models here.

#ONE-TO-MANY relationship tables
class Customer2(models.Model):
    name = models.CharField(max_length=255)

class Vehicle2(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer2, on_delete=models.CASCADE, related_name='Vehicle2')