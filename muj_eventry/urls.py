"""muj_eventry URL Configuration

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
from events import views
from clubs import viewsClub
from members import viewsUser
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events/add', views.CompleteEventSet)
router.register(r'clubs/add', viewsClub.CompleteClubSet)
router.register(r'users/add', viewsUser.CompleteUserSet)
# router.register(r'^clubs/(?P<name>\w{0,50})/$', viewsUser.FilteredEventSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'events/$', views.EventList, name='events'),
    url(r'^clubs/(?P<name>\w{0,50})/$', viewsUser.FilteredUserList, name='list'),
    # url(r'^events/events', views.CompleteEventListSet)
]
