from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from .models import Student, Teacher


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def sgn_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return HttpResponse("<h1>Login Failed</h1>")
    return render(request, "login_page.html")


def user_logout(request):
    logout(request)
    return redirect('signin')


def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                 password=pwd)
        # return to login page
        return redirect('signin')
    return render(request, 'registration.html')


def sample_json_response(request):
    data = {
        "message": "This is An API Call, Hello Next JS, From Django"
    }
    return JsonResponse(data)


def profile(request):
    return render(request, 'profile.html')
