from django.db import models


# Create your models here.
class Vaccine(models.Model):
    name = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=200)
    cnic_number = models.CharField(max_length=13)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
