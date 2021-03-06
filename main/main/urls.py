"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from real_quest.views import *
from rest_framework.authtoken import views as ww

router = routers.DefaultRouter()
router.register(r'profiles', UserModelViewSet, base_name="users")
router.register(r'queststages', QuestStagesViewSet, base_name="qstages")
router.register(r'questmodel', QuestModelViewSet, base_name="qmodel")
router.register(r'party', PartyModelViewSet, base_name="partym")
# router.register(r'chat', ChatView, base_name="chatview")

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', ww.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^chat/', ChatView.as_view(), name='chatview')
]
