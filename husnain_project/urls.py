from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('husnain_app.urls')),
    path('api/', include('api.urls')),
    path('covid/', include('covid_app.urls')),
]
