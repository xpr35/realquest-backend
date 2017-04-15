from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="auth_model")
    balance = models.FloatField()


class QuestStages(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255,
                              choices=[("Waiting", "waiting"), ("In Progress", "in_progress"), ("Done", "done")])
    cost = models.FloatField()  # ToDO currencies
    proof = models.FileField(null=True, blank=True)
    quest = models.ForeignKey('QuestModel', related_name='stages', null=True, blank=True)


class QuestModel(models.Model):
    producer = models.OneToOneField(UserModel, on_delete=models.SET_NULL, null=True, related_name="producer_model")
    consumer = models.OneToOneField(UserModel, on_delete=models.SET_NULL, null=True, related_name="consumer_model")
    create_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tags = models.CharField(max_length=30)


class PartyModel(models.Model):
    users = models.ForeignKey(UserModel)
    status = models.CharField(max_length=255, choices=[("Empty", "empty"), ("Not Full", "not_full"), ("Full", "full")])
    leader = models.OneToOneField(UserModel, on_delete=models.SET_NULL, null=True, related_name="leader_model")
