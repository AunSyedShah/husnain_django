from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    stud_class = models.IntegerField()
