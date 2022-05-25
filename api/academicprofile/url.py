from django import views
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from academicprofile.views import UserProfileView
from academicprofile.models import UserProfile

urlpatterns =[
    path('auth/academicprofile/', academicprofileView.as_view()),
]