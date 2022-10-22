from django.shortcuts import render

from .models import Student


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact_us.html')
