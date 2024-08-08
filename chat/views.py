from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile, ChatRoom
from .serializers import ChatRoomSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet


def index(req):
    return render(req, 'index.html')


class ApiProfile(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ApiChatRoom(ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
