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