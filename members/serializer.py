from rest_framework import serializers
from .models import user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= user
        fields=('Name','regNo', 'clubName1','clubName2','clubName3','clubName4')