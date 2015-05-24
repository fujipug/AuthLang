from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', 'main.views.views.home', name='home'),
                        url(r'^content/(?P<id>\d+)/$',
                            'main.views.views.content_details'),
                        url(r'^difficulty/(?P<difficulty_slug>[\w-]+)/$',
                            'main.views.views.difficulty'),
                        url(r'^country/(?P<country_slug>[\w-]+)/$',
                            'main.views.views.country'),
                        #url(r'^theme/(?P<theme_slug>[\w-]+)/$',
                        #    'main.views.views.theme'),
                        url(r'^difficulty/(?P<difficulty_slug>[\w-]+)/theme/(?P<theme_slug>[\w-]+)/$',
                            'main.views.views.difficulty_theme'),
                        url(r'^country/(?P<country_slug>[\w-]+)/theme/(?P<theme_slug>[\w-]+)/$',
                            'main.views.views.country_theme'),
                        url(r'^contentform/', 'main.views.views.content_manager'),
                        url(r'^themeform/', 'main.views.views.theme_manager'),
                        url(r'^countryform/', 'main.views.views.country_manager'),
                        url(r'^difficultyform/', 'main.views.views.country_manager'),
                        )