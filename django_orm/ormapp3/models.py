from django.db import models

# Create your models here.

#MANY-TO-MANY relationship tables
class Worker3(models.Model):
    name = models.CharField(max_length=255)

class Machine3(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(Worker3, related_name='Machine3')