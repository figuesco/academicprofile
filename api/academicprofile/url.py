from django import views
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from academicprofile.views import academicprofileView
from academicprofile.models import academicprofile

urlpatterns =[
    path('auth/academicprofile/', academicprofileView.as_view()),
]