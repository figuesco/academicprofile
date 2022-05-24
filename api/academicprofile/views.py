from django.shortcuts import render

# Create your views here.
from urllib import request, response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from django.conf import settings

from users.models import User
from academicprofile.models import UserProfile

from academicprofile.serializers import UserProfileSerializer

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    user = User.objects.filter(is_active=True)

    def post(self, request):
        data = request.data
        serializer = UserProfileSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        name = serializer.data["name"]
        institution = serializer.data["institution"]
        duration = serializer.data["duration"]

        user_id = request.user.id

        user_profile = UserProfile.objects.Create(
            user_id=user_id,
            name=name,
            institution=institution,
            duration=duration

        )

        user_profile.save()

        response = {
            "success": "Guardado satisfactorio",
            "status": status.HTTP_200_OK
        }
        return Response(response)




