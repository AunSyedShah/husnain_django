from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(default=0, primary_key=True)
    student_name = models.CharField(max_length=30, default="")
    father_name = models.CharField(max_length=30, default="")
    stud_class = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class IDCard(models.Model):
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
