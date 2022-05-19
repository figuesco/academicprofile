from genericpath import exists
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

# Para los tokens
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse
import jwt
from users.utils import Util
from django.conf import settings
from django.contrib.auth import authenticate

from ast import Return
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from datetime import datetime
import json

from users.serializers import UserSignupSerializer, UserLoginSerializer



"""
    User login.  Input example:
    {
        "email":"email@email.com",
        "password": "mysuperpassword"
    }
"""
# SIGNUP
class UserSignupView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = 'Gracias por registrarte a Get Talent, por favor verifica tu correo electrónico en la siguiente liga:\n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Get Talent, Confirma tu correo electrónico'}
        Util.send_email(data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# VERIFICAR EMAIL
class VerifyEmail(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])

            if not user.is_verified:
                user.is_verified = True
                user.save()

            if not user.is_active:
                user.is_active = True
                user.save()

            return Response({'email':'Cuenta activada exitosamente'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'email':'La liga de activación expiró'}, status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.DecodeError as identifier:
            return Response({'email':'Token inválido'}, status=status.HTTP_400_BAD_REQUEST)

# LISTA DE USUARIOS 
class ResourceView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        user = User.objects.filter(is_verified=True)
        serializer = UserSignupSerializer(user, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)   

# LOGIN

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
     
class UserLoginView(APIView):
    permission_classes = (AllowAny, )
  
    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.data['email']
        password=serializer.data['password']
        user=authenticate(username=email, password=password)
        if user:
            tokens = get_tokens_for_user(user)
            data = {
                'msg':'Exitosamente logueado',
                'tokens':tokens
            }   
            return Response(data, status=status.HTTP_200_OK)
    
#Valida si el correo existe
        user_email = User.objects.filter(email=email)
        if not user_email.exists():
            raise ValidationError({'msg':'No existe una cuenta relacionada al correo electrónico ingresado.'})
    
#Valida si el email ya está verificado
        user_active = User.objects.get(email=email)
        if user_active.is_active == False:
            raise ValidationError({'msg':'Tu cuenta no ha sido activada, verifica tu correo electrónico.'})

#Valida si la contraseña es correcta
        user = User.objects.get(email=email)
        while user.login_attempts < 3:
            while not User.objects.filter(password=password):
                user.login_attempts +=1
                user.save()
                raise ValidationError({'msg':'Contraseña incorrecta.'})
        else:
            user.is_active = False
            user.save()
            raise ValidationError({'msg':'Tu cuenta ha sido bloqueda.'})