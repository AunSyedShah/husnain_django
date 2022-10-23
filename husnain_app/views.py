from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
            return redirect("index")
        else:
            return redirect(request.path)
    return render(request, "login_page.html")
