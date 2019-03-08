# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse
from models import Activity
from projects.models import Project
from groups.models import Group
from forms import ActivityForm


# Create your views here.   

class Act_List(ListView):
   context_object_name = 'act_list'
   template_name = 'activ_list.html'
   def get_queryset(self):
      queryset_list = Activity.objects.all()
      return queryset_list
                                             
   
class Act_Create(CreateView):
   model = Activity
   form_class = ActivityForm
   template_name = 'activ_create.html'


class Act_Detail(DetailView):
   model = Activity
   template_name = 'activ_detail.html'
   context_object_name = 'act'
   def get_context_data(self, **kwargs):
        context = super(Act_Detail, self).get_context_data(**kwargs)
        return context

class Act_Update(UpdateView):
   model = Activity
   form_class = ActivityForm
   template_name = 'activ_create.html'

class Act_Delete(View):
    
    def get(self, request, pk):
      obj = Activity.objects.get(pk=pk)
      obj.delete()
      messages.error(request, 'Removido com sucesso!')
      return redirect('groups:list')

    def post(self, request, pk):
        return redirect('groups:list')

def ajax_load_groups(request):
   project = request.GET.get('project', None)
   groups = Group.objects.filter(project_id=project)
   return render(request, 'group_dropdown_list_options.html', {'groups': groups})
      



