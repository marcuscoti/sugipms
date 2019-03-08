# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, ButtonHolder, Button, HTML
from django import forms
from .models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class GroupEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(GroupEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'project-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(Div('name', css_class="col-6"), Div('project', css_class="col-3"), css_class="row"),
            Div(Div('description', css_class="col-6"), css_class="row"),
                ButtonHolder(Submit('submit', 'Salvar', css_class='button white'),
                             HTML("<a class='btn btn-danger' href='/groups/' role='button'>Cancelar</a>"), css_class='col-6')
            )
    
    class Meta:
        model = Group
        exclude = ['updated', 'created']

        labels = {
            'name': 'Nome',
            'description' : 'Descrição',
            'project' : 'Projeto',
        }
        

class GroupAddForm(GroupEditForm):

    def clean(self, *args, **kwargs):
        super(GroupAddForm, self).clean(*args, **kwargs)
        name = self.cleaned_data['name']
        project = self.cleaned_data['project']
        query = Group.objects.filter(name=name, project=project)
        if query.count() > 0:
            raise forms.ValidationError("Já existe esse grupo no projeto!")
        else:
            return self.cleaned_data
    





        
