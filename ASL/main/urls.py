from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', 'main.views.views.home', name='home'),
                        url(r'^content/(?P<id>\d+)/$',
                            'main.views.views.content_details'),
                        url(r'^(?P<category_slug>[\w-]+)/$',
                            'main.views.views.category_details'),
                        url(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/$',
                            'main.views.views.subcategory_details'),
                        # url(r'^contentform/', 'main.views.views.content_manager'),
                        # url(r#'^categoryform/', 'main.views.views.theme_manager'),
                        # url(r'^categorytypeform/', 'main.views.views.country_manager'),
                        # url(r'^contentcategoryform/', 'main.views.views.country_manager'),
                        # url(r'^contentsubcategoryform/', 'main.views.views.country_manager'),
                        # url(r'^subcategoryform/', 'main.views.views.country_manager'),
                        )