from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField( default = 18)
    email = models.EmailField( max_length = 20, unique = True)
    enrollment_date = models.DateField( auto_now_add = True)
