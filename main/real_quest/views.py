from django.shortcuts import render
from django.core.cache import cache
from rest_framework import viewsets
from .models import *
from .serializers import *
import django_filters
from rest_framework import views
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class QuestStagesViewSet(viewsets.ModelViewSet):
    queryset = QuestStages.objects.all()
    serializer_class = QuestStagesSerializer


class QuestFilter(django_filters.rest_framework.FilterSet):
    customer = django_filters.NumberFilter(name='consumer__id')

    class Meta:
        model = QuestModel
        fields = ['consumer']


class QuestModelViewSet(viewsets.ModelViewSet):
    queryset = QuestModel.objects.all()
    serializer_class = QuestModelSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = QuestFilter


class PartyModelViewSet(viewsets.ModelViewSet):
    queryset = PartyModel.objects.all()
    serializer_class = PartyModelSerializer


class ChatView(views.APIView):
    queryset = "test"
    def list(self, request):
        if 'chat' not in cache:
            cache.set('chat', [])
        if not isinstance(cache.get('chat'), list):
            cache.set('chat', [])
        return JsonResponse(cache.get('chat'))

    def create(self, request):
        if 'chat' not in cache:
            cache.set('chat', [])
        if not isinstance(cache.get('chat'), list):
            cache.set('chat', [])
        tmp = request.POST.dict()
        msg = tmp['msg']
        user = tmp['user']
        cache.set(cache.get('chat').append({'user': user, 'msg': msg}))
