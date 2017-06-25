from django.shortcuts import render
from .models import clubs
from django.core import serializers
from rest_framework import viewsets
from .serializer import ClubSerializer


class CompleteClubSet(viewsets.ModelViewSet):
    queryset = clubs.objects.all()
    serializer_class = ClubSerializer
    # return render(request, )
def ClubList(request , name):
    quer = clubs.objects.all()
    return render(request, 'clubs/clubs.html', {'events': quer})

# Create your views here.
