# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from models import Group, GroupStatus
from forms import GroupAddForm, GroupEditForm


# Create your views here.   

class Group_List(ListView):
   context_object_name = 'group_list'
   template_name = 'group_list.html'
   def get_queryset(self):
      queryset_list = Group.objects.all()
      return queryset_list
                                             
   
class Group_Create(CreateView):
   model = Group
   form_class = GroupAddForm
   template_name = 'group_create.html'


class Group_Detail(DetailView):
   model = Group
   template_name = 'group_detail.html'
   context_object_name = 'group'
   def get_context_data(self, **kwargs):
        context = super(Group_Detail, self).get_context_data(**kwargs)
        return context

class Group_Update(UpdateView):
   model = Group
   form_class = GroupEditForm
   template_name = 'group_create.html'

class Group_Delete(View):
    
    def get(self, request, pk):
      obj = Group.objects.get(pk=pk)
      obj.delete()
      messages.error(request, 'Removido com sucesso!')
      return redirect('groups:list')

    def post(self, request, pk):
        return redirect('groups:list')





      



