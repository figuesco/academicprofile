from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from academicprofile.views import academicprofileView

from users.views import UserSignupView, ResourceView, VerifyEmail, UserLoginView



urlpatterns = [
    path('auth/signup/',UserSignupView.as_view()),
    path('auth/registers/',ResourceView.as_view()),
    path('email-verify/',VerifyEmail.as_view(), name="email-verify"),
    path('auth/login/',UserLoginView.as_view(),name ="login"),
    path('auth/academicprofile/',academicprofileView.as_view()),
   ]