from rest_framework import seralizers
from academicprofile.models import UserProfile
from users.models import User

class UserProfileSerializer(seralizers.ModelSerializer):
    name = serializers.CharField()
    institution = serializers.CharField()
    duration = serializers.Charfield()

#Me falta: nivel(lista precargada), estatus(lista precargada)

class Meta:
    model:UserProfile
    fields = ['name', 'institution', 'duration']
