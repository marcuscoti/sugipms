# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, ButtonHolder, Button, HTML
from django import forms
from .models import Activity
from projects.models import Project
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class ActivityForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.none()
        self.helper = FormHelper()
        self.helper.form_id = 'act-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(Div('action', css_class="col-6"), Div('project', css_class="col-3"), Div('group', css_class="col-3"), css_class="row"),
            Div(Div('data_center', css_class="col-3"), Div('local', css_class="col-3"), css_class="row"),
            Div(Div('start_estimated', css_class="col-3"),
                Div('duration_estimated', css_class="col-3"),
                Div('end_estimated', css_class="col-3"),
                Div('status', css_class="col-3"), css_class="row"),
                ButtonHolder(Submit('submit', 'Salvar', css_class='button white'),
                             HTML("<a class='btn btn-danger' href='/acts/' role='button'>Cancelar</a>"), css_class='col-6')
            )
        
        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['group'].queryset = Group.objects.filter(project_id=project_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['group'].queryset = Group.objects.filter(project=self.instance.project)
            
    class Meta:
        model = Activity
        exclude = ['updated', 'created']

        labels = {
            'project': 'Projeto',
            'group': 'Grupo',
            'action' : 'Ação',
            'status' : 'Status',
            'duration_estimated' : 'Duração (estimada)',
            'start_estimated' : 'Inicio (estimado)',
            'end_estimated' : 'Término (estimado)',
            'data_center' : 'Data Center',
            'local' : 'Local',
        }