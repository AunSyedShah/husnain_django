from django.http import JsonResponse


# Create your views here.
def home(request):
    data = {
        "message": "Welcome Husnain",
    }
    return JsonResponse(data)
