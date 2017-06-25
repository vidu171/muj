from rest_framework import serializers
from .models import clubs

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= clubs
        fields=('clubName','clubUserUrl','clubLogo','clubAdmin')