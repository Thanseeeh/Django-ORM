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

# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="Roald Dahl")


# Then hook it into the Book model explicitly.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    objects = models.Manager()  # The default manager.
    dahl_objects = DahlBookManager()  # The Dahl-specific manager.

#With this sample model, Book.objects.all() will return all books in the database, but Book.dahl_objects.
# all() will only return the ones written by Roald Dahl.

#Raw Method
#the raw() method allows you to execute raw SQL queries directly against your database. it provides a way to perform database
#operations that may not be easily achievable or optimized using the ORM's high-level query APIs
from django.db import connection

query = "SELECT id, username FROM myapp_student"
raw_queryset = Student.objects.raw(query)

for student in raw_queryset:
    print(student.username)

#Cursor Method
#In Django, the cursor() method allows you to directly access the database cursor associated with a database connection. 
#The cursor provides a low-level interface to execute raw SQL queries and fetch results from the database.
from django.db import connection

cursor = connection.cursor()
cursor.execute("SELECT * FROM myapp_student")

rows = cursor.fetchall()

for row in rows:
    print(row)

#Bulk Create method
#In Django ORM, the bulk_create() method allows you to efficiently create multiple model objects in a single database query. 
#It is a performance optimization technique that can significantly reduce the overhead of individual database queries when you need to create a 
#large number of objects.

from myapp.models import Teacher, Student

Student.objects.bulk_create([
    Student(username = 'hamdan03', first_name = 'hamdan', last_name = 'swalih', mobile = '9988341287', email = 'hamdan@gmail.com'), 
    Student(username = 'ridhinbro', first_name = 'ridin', last_name = 'k', mobile = '9847924232', email = 'ridin@gmail.com')])

#Exclude method
queryset = Student.objects.exclude(username__startswith = 'a')
print(queryset)

#Contians method
#The contains lookup checks if a field value contains a specific substring. It performs a case-sensitive match.

query = Student.objects.filter(field__contains='substring')
print(query)