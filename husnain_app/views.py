from django.shortcuts import render

from .models import Student


# Create your views here.
def home(request):
    if request.method == "POST":
        if "add_student" in request.POST:
            roll_no = request.POST.get('roll_no')
            stud_name = request.POST.get('stud_name')
            father_name = request.POST.get('father_name')
            stud_class = request.POST.get('stud_class')
            Student.objects.create(roll_no=roll_no, student_name=stud_name, father_name=father_name,
                                   stud_class=stud_class)
        if "delete_student" in request.POST:
            roll_no = request.POST.get('roll_no')
            try:
                Student.objects.get(roll_no=roll_no).delete()
            except:
                pass
        if "update_student" in request.POST:
            roll_no = request.POST.get('roll_no')
            stud_name = request.POST.get('stud_name')
            father_name = request.POST.get('father_name')
            stud_class = request.POST.get('stud_class')
            try:
                student_old = Student.objects.get(roll_no=roll_no)
                student_old.student_name = stud_name
                student_old.father_name = father_name
                student_old.stud_class = stud_class
                student_old.save()
            except:
                pass
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
    # return JsonResponse(context)
    return render(request, "calculator.html", context)
