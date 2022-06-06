from rest_framework import serializers
from academicprofile.models import academicprofile
from users.models import User


class academicprofileSerializer(serializers.ModelSerializer):
    level = serializers.CharField()
    name = serializers.CharField()
    institution = serializers.CharField()
    duration = serializers.CharField()
    status_academic = serializers.CharField()

class Meta:
    model = academicprofile
    fields = ['level', 'name', 'institution', 'duration', 'status_academic']
