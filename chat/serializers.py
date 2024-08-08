from rest_framework import serializers
from .models import Profile, ChatRoom
from django.contrib.auth.models import User


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'avatar', 'room')