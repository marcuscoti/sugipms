# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import Act_List, Act_Create, Act_Detail, Act_Update, Act_Delete, ajax_load_groups

urlpatterns = [
    url(r'^$', Act_List.as_view(), name='list'),
    url(r'^create/$', Act_Create.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)$', Act_Detail.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', Act_Update.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$', Act_Delete.as_view(), name='delete'),
    url(r'^ajax/load-groups/$', ajax_load_groups, name='ajax_load_groups'),
]
