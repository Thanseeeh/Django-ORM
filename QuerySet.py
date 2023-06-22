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