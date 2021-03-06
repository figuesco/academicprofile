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

        name = serializer.data["name"]
        education_level = serializer.data["education_level"]
        institution = serializer.data["institution"]
        duration = serializer.data["duration"]
        status_academic = serializer.data ["status_academic"]

        user_id = request.user.id

        academic_profile = academicprofile.objects.create(
            user_id=user_id,
            name=name,
            education_level=education_level,
            institution=institution,
            duration=duration,
            status_academic=status_academic

        )

        academic_profile.save()

        response = {
            "success": "Datos personales guardados correctamente",
            "status": status.HTTP_200_OK
        }
        return Response(response)
    
    def find_answers(request):
        id_profile = request.Get.get('id')
        profile = perfil_academic.objects.filter(perfil_id=id)
        for ex in profile:
            academic_profile = academic_profile.objects.filter(id= ex.profile_id)
            academic_profile = list(academic_profile.values())
        return jsonResponse({'academicprofile': academic_profile})

    def find_answers(request):
        return {
            'id': academic_profile.codigo,
            'name': academic_profile.name,
            'education_level':academic_profile.education_level,
            'institution':academic_profile.institution,
            'duration': academic_profile.duration,
            'status_academic':academic_profile.status_academic
        }
        
        academic_profile.save()

        response = {
            "success": "Datos personales guardados correctamente",
            "status": status.HTTP_200_OK
        }
        return Response(response)

    def get(self, request):
        academic_profile = academicprofile.objects.filter(user_id = request.user.id)
        serializer = academicprofileSerializer(academic_profile, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK) 

 
