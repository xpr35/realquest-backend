from django.contrib import admin
from .models import *


class UserModelAdmin(admin.ModelAdmin):
    pass

class QuestStagesAdmin(admin.ModelAdmin):
    pass

class QuestModelAdmin(admin.ModelAdmin):
    pass

class PartyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(QuestStages, QuestModelAdmin)
admin.site.register(QuestModel, QuestModelAdmin)
admin.site.register(PartyModel, PartyModelAdmin)
