from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.name
