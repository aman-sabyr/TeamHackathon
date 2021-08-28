from django.shortcuts import render
from rest_framework.views import APIView
from .models import Chat


class ChatView(APIView):
    def get(self, request):
        queryset = Chat.objects.all()

