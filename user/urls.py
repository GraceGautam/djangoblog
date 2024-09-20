from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),  # Ensure there is no leading/trailing space or quote
    
]







