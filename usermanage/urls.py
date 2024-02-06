# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manageuser2.urls')),  # Include your app's URLs
    # Add more project-wide URL patterns as needed
]