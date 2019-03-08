# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Project, ProjectStatus

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
   class Meta:
      model = Project
      list_display = ('name', 'description',)
      #list_display_links = ('name',)
      #list_filter = ('leader', 'state',)
      #search_filters = ('name', 'description',)

class ProjectStatusAdmin(admin.ModelAdmin):
   class Meta:
      model = ProjectStatus

      list_display = ('project', 'act_ended', 'act_program', 'act_late', 'act_total', 'deliveried', 'target')
      list_display_links = ('project',)
      list_filter = ('project',)
      
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
