from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.views.home', name='home'),
    url(r'^pages/$', 'main.views.views.pages'),
    url(r'^facil/$', 'main.views.views.facil_list'),
)