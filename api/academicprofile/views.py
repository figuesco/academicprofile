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
from academicprofile.models import  academicprofile

from academicprofile.serializers import academicprofileSerializer

class academicprofileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    user = User.objects.filter(is_active=True)

    def post(self, request):
        data = request.data
        serializer = academicprofileSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        level = serializer.data ["level"]
        name = serializer.data["name"]
        institution = serializer.data["institution"]
        duration = serializer.data["duration"]
        status = serializer.data ["status"]

        user_id = request.user.id

        academicprofile = academicprofile.objects.Create(
            user_id=user_id,
            level=level,
            name=name,
            institution=institution,
            duration=duration,
            status=status

        )

        academicprofile.save()

        response = {
            "success": "Guardado satisfactorio",
            "status": status.HTTP_200_OK
        }
        return Response(response)




