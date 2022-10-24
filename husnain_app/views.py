from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .models import Student


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
            return HttpResponse("<h1>Login Successful</h1>")
        else:
            return HttpResponse("<h1>Login Failed</h1>")
    return render(request, "login_page.html")


def user_logout(request):
    logout(request)
    return redirect('signin')
