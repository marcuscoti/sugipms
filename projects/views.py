# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from models import Project, ProjectStatus
from forms import ProjectForm


# Create your views here.   

class Projects_List(ListView):
   context_object_name = 'project_list'
   template_name = 'project_list.html'
   def get_queryset(self):
      queryset_list = Project.objects.all()
      return queryset_list
                                             
   
class Projects_Create(CreateView):
   model = Project
   form_class = ProjectForm
   template_name = 'project_create.html'


class Project_Detail(DetailView):
   model = Project
   template_name = 'project_detail.html'
   context_object_name = 'project'
   def get_context_data(self, **kwargs):
        context = super(Project_Detail, self).get_context_data(**kwargs)
        return context

class Project_Update(UpdateView):
   model = Project
   form_class = ProjectForm
   template_name = 'project_create.html'

class Project_Delete(View):
    
    def get(self, request, pk):
      obj = Project.objects.get(pk=pk)
      obj.delete()
      messages.error(request, 'Removido com sucesso!')
      return redirect('projects:list')

    def post(self, request, pk):
        return redirect('projects:list')





      



