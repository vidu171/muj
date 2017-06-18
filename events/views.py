from django.shortcuts import render
from .models import events
from django.core import serializers
from rest_framework import viewsets
from .serializer import EventSerializer

def home(request):
    return render(request, 'event/home.html', {'datas': 0})


class CompleteEventSet(viewsets.ModelViewSet):
    queryset = events.objects.all()
    serializer_class = EventSerializer
    # return render(request, )
def EventList(request):
    quer = events.objects.all()
    return render(request, 'event/events.html', {'events': quer})