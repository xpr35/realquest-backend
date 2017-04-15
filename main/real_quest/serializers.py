from rest_framework import serializers
from .models import *


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class QuestStagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestStages
        fields = '__all__'
        depth = 3


class QuestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestModel
        fields = '__all__'
        depth = 3


class PartyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyModel
        fileds = '__all__'
