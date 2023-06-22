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