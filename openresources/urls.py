# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from openresources import views

from openresources.models import Tag

# commenting out autocomplete stuff for now, probably needs custom implementation
#from autocomplete.views import autocomplete

#autocomplete.register(
#    id = 'keys',
#    queryset = Tag.objects.values('key').distinct(),
#    fields = ('key',),
#    limit = 20,
#    key = 'key',
#    label = 'key',
#)

urlpatterns = patterns('',
    url(r'^$', views.index, name='openresources_index'),

    url(r'^views/$', views.views, name='openresources_views'),
    url(r'^view/(?P<name>.*)/(?P<mode>.*)/$', views.view, name='openresources_view'),
    url(r'^view/(?P<name>.*)/$', views.view, name='openresources_view'),
    url(r'^views/new/$', views.edit_view, name='openresources_new_view'),
    url(r'^views/edit/(?P<name>.*)/$', views.edit_view, name='openresources_edit_view'),

    url(r'^templates/$', views.templates, name='openresources_templates'),
    url(r'^templates/new/$', views.edit_template, name='openresources_template_edit'),
    url(r'^template/(?P<name>.*)/$', views.edit_template, name='openresources_template_edit'),
    # temporary, until resource view support assigned template
    url(r'^template-resource/(?P<template>.*)/(?P<resource>.*)/$', views.edit_with_template, name='openresources_edit_with_template'),
    url(r'^template-resource/(?P<template>.*)/$', views.edit_with_template, name='openresources_edit_with_template'),

    url(r'^all/$', views.all_resources, name='openresources_all'),
   
    url(r'^tags/$', views.tags, name='openresources_tags'),
    # *? matches key non-greedy, matching only as few as possible characters if value has = sign in it
    url(r'^tag/(?P<key>.*?)=(?P<value>.*)/$', views.tag, name='openresources_tag'),
    url(r'^tag/(?P<key>.*)/$', views.tag, name='openresources_tag_key'),
    url(r'^tools/rename_tag/$', views.rename_tag, name='openresources_rename_tag'),

    url(r'^icons/$', views.icons, name='openresources_icons'),
    url(r'^icons/add/$', views.add_icon, name='openresources_new_icon'),

    url(r'^choices.json$', views.resource_choices),
    url(r'^tag/(?P<key>.*)/choices.json$', views.tag_choices),
    
    url(r'^json/view/(?P<name>.*)/$', views.view_json, name='geojson'),
    
    # *? matches key non-greedy, matching only as few as possible characters if value has '=' sign in it
    url(r'^with/tag/(?P<key>.*?)=(?P<value>.*)/$', views.resources_by_tag, name='openresources_with_tag'),
    url(r'^with/tag/(?P<key>.*)/$', views.resources_by_tag, name='openresources_with_key'),
    url(r'^resource/(?P<key>.*)/$', views.resource, name='openresources_resource'),
    url(r'^new/$', views.edit_resource, name='openresources_new'),
    url(r'^edit/(?P<key>.*)/$', views.edit_resource, name='openresources_edit'),
    #url('^autocomplete/(\w+)/$', autocomplete, name='autocomplete'),

    url(r'^context/set/$', views.set_context, name='openresources_set_context'),
    url(r'^search/$', views.search, name='openresources_search'),
    url(r'^credits/$', direct_to_template, {'template': 'openresources/credits.html'}, name='openresources_credits'),

)
