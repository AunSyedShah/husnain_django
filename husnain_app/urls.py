from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_us, name="contact_us"),
    path('login/', views.sgn_in, name="signin"),
    path('logout/', views.user_logout, name="logout"),
    path('registration/', views.registration, name="registration"),
    path('sample_json/', views.sample_json_response, name="sample_json"),
    path('profile/', views.profile, name="profile"),
]
