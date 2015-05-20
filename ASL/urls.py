from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'ASL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ASL.views.views.home', name='home'),
    url(r'^pages/$', 'ASL.views.views.pages'),
    url(r'^facil/$', 'ASL.views.views.facil_list'),
]
