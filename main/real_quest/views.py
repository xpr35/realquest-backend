from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    # permission_classes = [TokenAuthentication]


class QuestStagesViewSet(viewsets.ModelViewSet):
    queryset = QuestStages.objects.all()
    serializer_class = QuestStagesSerializer
    # permission_classes = [TokenAuthentication]


class QuestModelViewSet(viewsets.ModelViewSet):
    queryset = QuestModel.objects.all()
    serializer_class = QuestModelSerializer
    # permission_classes = [TokenAuthentication]


class PartyModelViewSet(viewsets.ModelViewSet):
    queryset = PartyModel.objects.all()
    serializer_class = PartyModelSerializer
    # permission_classes = [TokenAuthentication]
