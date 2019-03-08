# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from projects.models import Project
from groups.models import Group

User = get_user_model()

# Create your models here.
class Activity(models.Model):

   STATUS_C = (
      ('on', 'Programado'),
      ('end', 'Concluído'),
      ('wip', 'Em Andamento'),
   )

   DATACENTER_C = (
      ('Norte', 'Norte'),
      ('Sul', 'Sul'),
   )
   
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   group = models.ForeignKey(Group, on_delete=models.CASCADE)
   action = models.CharField(max_length=30)
   status = models.CharField(max_length=3, choices=STATUS_C, default='on')
   duration_estimated = models.IntegerField(default=1, validators=[MinValueValidator(1),])
   start_estimated = models.DateField()
   end_estimated = models.DateField()
   data_center = models.CharField(max_length=8, choices=DATACENTER_C, default='Norte')
   local = models.CharField(max_length=15, default='na')
   start_real = models.DateField(null=True, blank=True)
   end_real = models.DateField(null=True, blank=True)
   duration_real = models.IntegerField(null=True, blank=True)
   late = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __unicode__(self):
      return self.action

   def __str__(self):
      return self.action

   def get_absolute_url(self):
      return reverse('activities:list')

   def get_status(self):
      for value in self.STATUS_C:
         if value[0] == self.status:
            return value[1]

   def get_data_center(self):
      for value in self.DATACENTER_C:
         if value[0] == self.data_center:
            return value[1]

   def get_late(self):
      if self.late:
         return "Sim"
      else:
         return "Não"


   
