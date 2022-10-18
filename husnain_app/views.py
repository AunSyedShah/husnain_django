from django.shortcuts import render
from .models import Student


# Create your views here.
def home(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, "index.html", context)


def calculator(request, num1, num2):
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2
    context = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    return render(request, "calculator.html", context)
