from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email =models.EmailField(unique=True)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name