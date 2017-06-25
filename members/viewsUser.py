from django.shortcuts import render
from .models import user
from rest_framework import viewsets, generics
from .serializer import UserSerializer
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from itertools import chain


class CompleteUserSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    # return render(request, )


def UserList(request, name):
    quer = user.objects.all()
    return render(request, 'event/events.html', {'events': quer})


def FilteredUserList(request, name):
    list1 = user.objects.filter(clubName1=name)
    list2 = user.objects.filter(clubName2=name)
    list3 = user.objects.filter(clubName3=name)
    list4 = user.objects.filter(clubName4=name)
    result = list(chain(list1, list2,list3, list4))
    jsonSerializer = serializers.get_serializer("json")()
    response = jsonSerializer.serialize(result, ensure_ascii=False, indent=4)
    return HttpResponse(response)
    # queryset = get_queryset()
    serializer_class = UserSerializer

# Create your views here.
