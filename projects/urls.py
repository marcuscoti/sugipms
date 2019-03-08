# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import Projects_List, Projects_Create, Project_Detail, Project_Update, Project_Delete

urlpatterns = [
    url(r'^$', Projects_List.as_view(), name='list'),
    url(r'^create/$', Projects_Create.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)$', Project_Detail.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', Project_Update.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$', Project_Delete.as_view(), name='delete'),
]
