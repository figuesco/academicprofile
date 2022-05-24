from rest_framework import seralizers
from academicprofile.models import UserProfile
from users.models import User

class UserProfileSerializer(seralizers.ModelSerializer):
    level = seralizers.CharField()
    name = serializers.CharField()
    institution = serializers.CharField()
    duration = serializers.Charfield()
    status = seralizers.Charfield()

class Meta:
    model:UserProfile
    fields = ['name', 'institution', 'duration']
