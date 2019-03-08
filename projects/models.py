# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Project(models.Model):

   STATE_C = (
      ('on', 'Em Andamento'),
      ('end', 'Concluído'),
      ('off', 'Cancelado/Arquivado'),
   )
   
   name = models.CharField(max_length=30)
   description = models.TextField(max_length=200)
   leader = models.ForeignKey(User)
   start_estimated = models.DateField()
   end_estimated = models.DateField()
   state = models.CharField(max_length=3, choices=STATE_C, default='on')
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __unicode__(self):
      return self.name

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('projects:list')

   def get_project_leader(self):
      name = self.leader.first_name  + " " + self.leader.last_name
      return name

   def get_project_state(self):
      for state in self.STATE_C:
         if state[0] == self.state:
            return state[1]

class ProjectStatus(models.Model):
   
   project = models.ForeignKey(Project)
   act_ended = models.IntegerField(default=0)
   act_program = models.IntegerField(default=0)
   act_late = models.IntegerField(default=0)
   act_total = models.IntegerField(default=0)
   deliveried = models.DecimalField(default=0, max_digits=2, decimal_places=2)
   target = models.DecimalField(default=0, max_digits=2, decimal_places=2)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   def __unicode__(self):
      return self.project.name

   def __str__(self):
      return self.project.name

   class Meta:
        verbose_name_plural = "ProjectStatus"

   
