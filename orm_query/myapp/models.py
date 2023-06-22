from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)