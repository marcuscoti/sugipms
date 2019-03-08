# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from views import Group_List, Group_Create, Group_Detail, Group_Update, Group_Delete

urlpatterns = [
    url(r'^$', Group_List.as_view(), name='list'),
    url(r'^create/$', Group_Create.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)$', Group_Detail.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', Group_Update.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$', Group_Delete.as_view(), name='delete'),
]
