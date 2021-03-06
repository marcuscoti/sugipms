# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Group, GroupStatus

# Register your models here.

class GroupAdmin(admin.ModelAdmin):
   class Meta:
      model = Group
      list_display = ('name', 'description',)
      #list_display_links = ('name',)
      #list_filter = ('leader', 'state',)
      #search_filters = ('name', 'description',)

class GroupStatusAdmin(admin.ModelAdmin):
   class Meta:
      model = GroupStatus

      #list_display = ('project', 'act_ended', 'act_program', 'act_late', 'act_total', 'deliveried', 'target')
      #list_display_links = ('project',)
      #list_filter = ('project',)
      
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupStatus, GroupStatusAdmin)
