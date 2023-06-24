# Start the Django shell by running the following command:
#  python manage.py shell


#Creating objects in the database
from myapp.models import Student

student1 = Student.objects.create(
    username='student1',
    first_name='John',
    last_name='Doe',
    mobile='1234567890',
    email='student1@example.com'
)
student2 = Student.objects.create(
    username='student2',
    first_name='Jane',
    last_name='Smith',
    mobile='9876543210',
    email='student2@example.com'
)

#Query all Student details
students = Student.objects.all()
print(students)

#Retrieving Single Objects from QuerySets
queryset = Student.objects.get(pk = 1)  
print(queryset)

#Filtering the Records
queryset = Student.objects.filter(username__startswith = 'a')
print(queryset)

# filetr options :
# 1. startswith:
#    Syntax: field__startswith=value
#    Example: objects.filter(title__startswith='A')
#    Retrieves objects where the specified field starts with the given value.

# 2. endswith:
#    Syntax: field__endswith=value
#    Example: objects.filter(title__endswith='Z')
#    Retrieves objects where the specified field ends with the given value.

# 3. contains:
#    Syntax: field__contains=value
#    Example: objects.filter(title__contains='book')
#    Retrieves objects where the specified field contains the given value.

#Exclude() method
queryset = Student.objects.exclude(username__startswith = 'a')
print(queryset)

#OR and AND operations
#OR:
queryset = Student.objects.filter(first_name__startswith = 'R') | Student.objects.filter(last_name__startswith = 'S')
print(queryset)
#AND:
queryset = Student.objects.filter(first_name__startswith = 'P') & Student.objects.filter(last_name__startswith = 'S')
print(queryset)

#Q object
from django.db.models import Q
queryset3 = Student.objects.filter(Q(first_name__startswith='R') & Q(last_name__startswith='D') ) #Q object AND operation
queryset3 = Student.objects.filter(Q(first_name__startswith='R') | Q(last_name__startswith='D') ) #Q object OR operation

#Bulk_Create() method
#sometimes we want to create multiple objects in one shot. django ORM provides the bulk_create to create multiple objects in one way.
Student.objects.bulk_create([
    Student(first_name = 'Jai', last_name = 'Shah', mobile = '88888', email = 'shah@reddif.com'),
    Student(first_name = 'Tarak', last_name = 'Mehta', mobile = '9999', email = 'tarak@reddif.com'),
    Student(first_name = 'SuryaKumar', last_name = 'Yadav', mobile = '00000', email = 'yadav@reddif.com')
    ])

#Aggregate methods
#these methods help to perform operations such as counting, summing, averaging, finding minimum or maximum.
from django.db.models import Avg, Count, Max, Min, Sum

Student.objects.all().aggregate(Sum('id')) #sum
Student.objects.all().aggregate(Avg('id')) #average
Student.objects.all().aggregate(Count('id')) #count
Student.objects.all().aggregate(Max('id')) #max
Student.objects.all().aggregate(Min('id')) #min

#Annotation methods
#Annotation of an object creates a separate summary for each object in a queryset. It is often used to obtain a summary of a particular object.
annotated_student = Student.objects.annotate(post_count=Count('id'))
annotated_student[1].post_count

# Difference between Django's Annotate and Aggregate Methods :-

# Annotate(), unlike aggregate(), is not a terminal clause. The annotate() clause returns a QuerySet. 
# Annotations are inherently linked to individual queryset items. 
# Aggregate result (summary) values across an entire QuerySet.

#Django values_list
#Django values_list() is an optimization to grab specific data from the database instead of building and loading the entire model instance.

Student.objects.values_list('id', 'first_name')
Student.objects.values_list('id', 'first_name').get(id=7)
Student.objects.values_list('id', 'first_name').filter(username__contains = 'a')

#Django managers
#A Manager is the interface through which database query operations are provided to Django models.
#At least one Manager exists for every model in a Django application.

#Manager names:
#By default, Django adds a Manager with the name objects to every Django model class. However, if you want to use objects as a field name, 
# or if you want to use a name other than objects for the Manager, you can rename it on a per-model basis. 
# To rename the Manager for a given class, define a class attribute of type models.Manager() on that model. For example:

from django.db import models


class Person(models.Model):
    # ...
    people = models.Manager()

#Using this example model, Person.objects will generate an AttributeError exception, but Person.people.all() will provide a list of all Person objects.

#Custom managers
#You can use a custom Manager in a particular model by extending the base Manager class and instantiating your custom Manager in your model.