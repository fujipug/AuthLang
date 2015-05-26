from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from main.views.views import ContentList, ContentDetail, DifficultyList, DifficultyDetail, CountryList, CountryDetail, CategoryTypeList, CategoryTypeDetail, CategoryList, CategoryDetail, ContentCategoryList, ContentCategoryDetail
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = patterns('',
                        url(r'^admin/', include(admin.site.urls)),
                        #
                        url(r'^searchtable/', 'main.views.views.search_table'),
                        url(r'^signin/', 'main.views.signin_manager.signin_manager'),
                        url(r'^logout/', 'main.views.signin_manager.user_logout'),
                        url(r'^$', 'main.views.views.home', name='home'),
                        #forms
                        url(r'^adminforms/', 'main.views.form_manager.admin_forms'),
                        url(r'^contentform/', 'main.views.form_manager.content_manager'),
                        url(r'^categoryform/', 'main.views.form_manager.category_manager'),
                        url(r'^categorytypeform/', 'main.views.form_manager.category_type_manager'),
                        url(r'^contentcategoryform/', 'main.views.form_manager.content_category_manager'),
                        url(r'^countryform/', 'main.views.form_manager.country_manager'),
                        url(r'^difficultyform/', 'main.views.form_manager.difficulty_manager'),
                        #end forms
                        #rest links
                        url(r'^data/contents/$', ContentList.as_view()),
                        url(r'^data/contents/(?P<pk>[0-9]+)/$', ContentDetail.as_view()),
                        url(r'^data/difficulties/$', DifficultyList.as_view()),
                        url(r'^data/difficulties/(?P<pk>[0-9]+)/$', DifficultyDetail.as_view()),
                        url(r'^data/countries/$', CountryList.as_view()),
                        url(r'^data/countries/(?P<pk>[0-9]+)/$', CountryDetail.as_view()),
                        url(r'^data/categorytypes/$', CategoryTypeList.as_view()),
                        url(r'^data/categorytypes/(?P<pk>[0-9]+)/$', CategoryTypeDetail.as_view()),
                        url(r'^data/categories/$', CategoryList.as_view()),
                        url(r'^data/categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),
                        url(r'^data/contentcategories/$', ContentCategoryList.as_view()),
                        url(r'^data/contentcategories/(?P<pk>[0-9]+)/$', ContentCategoryDetail.as_view()),
                        #end rest links
                        url(r'^(?P<category_type_slug>[\w-]+)/(?P<category_slug>[\w-]+)/$',
                            'main.views.views.content_list_by_category'),
                        )