# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from projects.models import Project

User = get_user_model()

# Create your models here.
class Group(models.Model):

   NAME_C = (
         ('CH', 'CABLING HORIZONTAL'),
         ('CV', 'CABLING VERTICAL'),
         ('HW', 'INSTALAÇÃO E CONFIGURAÇÃO DE HW'),
         ('INFRA', 'INFRA BÁSICA'),
         ('PLAN', 'PLANEJAMENTO'),
         ('SUGI', 'SUGI+ SERVIDORES'),
      )
   
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   name = models.CharField(max_length=8, choices=NAME_C, default='CH')
   description = models.TextField(max_length=60, null=True, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __unicode__(self):
      return self.get_group()

   def __str__(self):
      return self.get_group()

   def get_absolute_url(self):
      return reverse('groups:list')

   def get_group(self):
      for group in self.NAME_C:
         if group[0] == self.name:
            return group[1]

class GroupStatus(models.Model):

   group = models.ForeignKey(Group)
   start = models.DateField(default=timezone.now())
   end = models.DateField(default=timezone.now())
   duration = models.IntegerField(default=0)
   act_ended = models.IntegerField(default=0)
   act_program = models.IntegerField(default=0)
   act_late = models.IntegerField(default=0)
   act_total = models.IntegerField(default=0)
   deliveried = models.DecimalField(default=0, max_digits=2, decimal_places=2)
   target = models.DecimalField(default=0, max_digits=2, decimal_places=2)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   def __unicode__(self):
      return self.group.name

   def __str__(self):
      return self.group.name

   class Meta:
        verbose_name_plural = "GroupStatus"

   
