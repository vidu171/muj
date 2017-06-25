from rest_framework import serializers
from .models import events

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= events
        fields=('club','name','start_time','end_time','discription','addBanner1','addBanner2','addBanner3','addBanner4',
                'video1','video2','person_name_1','person_contact_1','person_name_2','person_contact_2'
                , 'created_date')