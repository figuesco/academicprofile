from rest_framework import serializers
from academicprofile.models import academicprofile



class academicprofileSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    education_level = serializers.CharField()
    institution = serializers.CharField()
    duration = serializers.CharField()
    status_academic= serializers.CharField()

    class Meta:
           model = academicprofile
           fields = ['name', 'education_level', 'institution', 'duration', 'status_academic']
              