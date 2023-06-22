from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.teacher_name}'

class Student(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    teacher_name = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)