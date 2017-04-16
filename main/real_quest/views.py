import json
import django_filters
from django.core.cache import cache
from rest_framework import views, viewsets
from .models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse


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


class ChatView(views.View):

    def get(self, request):
        if 'chat' not in cache:
            cache.set('chat', [])
        if not isinstance(cache.get('chat'), list):
            cache.set('chat', [])
        ret = cache.get('chat')
        # print(ret)
        return JsonResponse(ret, safe=False)

    def post(self, request):
        # url-encoded, not json data must be
        if 'chat' not in cache:
            cache.set('chat', [])
        if not isinstance(cache.get('chat'), list):
            cache.set('chat', [])
        tmp = json.loads(request.body.decode())
        msg = tmp.get('msg')
        user = tmp.get('user')
        original = cache.get('chat')
        original.append({'user': user, 'msg': msg})
        print(user, msg, original)
        cache.set('chat', original)
        return JsonResponse({})
