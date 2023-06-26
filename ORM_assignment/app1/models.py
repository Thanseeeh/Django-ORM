from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return self.name
    
class Employees(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    salary = models.IntegerField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    place = models.CharField(max_length=50)
    position = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name