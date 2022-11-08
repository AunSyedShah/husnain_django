from django.shortcuts import render, redirect
from .models import Vaccine, Profile


# Create your views here.
def index(request):
    context = {

    }
    if request.method == "POST":
        cnic_number = request.POST.get('cnic_number')
        record = Profile.objects.filter(cnic_number=cnic_number).exists()
        if record:
            profile = Profile.objects.get(cnic_number=cnic_number)
            vaccine = profile.vaccine
            print(vaccine.name)
            context["profile"] = profile
            return render(request, 'covid_app/index.html', context)
        else:
            print("No record found")
            return render(request, 'covid_app/index.html', {'error': 'Record not found'})
    return render(request, 'covid_app/index.html')
