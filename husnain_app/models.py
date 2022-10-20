from django.db import models


# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(default=0)
    student_name = models.CharField(max_length=30, default="")
    father_name = models.CharField(max_length=30, default="")
    stud_class = models.IntegerField(default=0)
