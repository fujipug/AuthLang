from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.views.home', name='home'),
    url(r'^content/(?P<id>\d+)/$', 'main.views.views.content_details'),
    url(r'^difficulty/(?P<difficulty_slug>[\w-]+)/$', 'main.views.views.difficulty'),
    url(r'^difficulty/(?P<difficulty_slug>[\w-]+)/theme/(?P<theme_slug>[\w-]+)/$', 'main.views.views.theme'),
)