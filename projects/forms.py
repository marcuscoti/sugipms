# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, ButtonHolder, Button, HTML
from django import forms
from .models import Project
from django.contrib.auth import get_user_model
User = get_user_model()


def get_User_Choices():
    user_choices = [('','-------------')]
    user_list = User.objects.all()
    for user in user_list:
        user_name = user.first_name + " " + user.last_name
        user_choices.append((user.id, user_name))
    return user_choices

class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        user_name = obj.first_name + " " + obj.last_name
        return user_name



class ProjectForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'project-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(Div('name', css_class="col-6"), Div('start_estimated', css_class="col-3"), Div('state', css_class="col-3"), css_class="row"),
            Div(Div('description', css_class="col-6"), Div('end_estimated', css_class="col-3"), Div('leader', css_class="col-3"), css_class="row"),
                ButtonHolder(Submit('submit', 'Salvar', css_class='button white'),
                             HTML("<a class='btn btn-danger' href='/projects/' role='button'>Cancelar</a>"), css_class='col-6')
            )
        
    leader = UserChoiceField(queryset=User.objects.all(), empty_label='-----')
    
    class Meta:
        model = Project
        exclude = ['updated', 'created']

        labels = {
            'name': 'Nome',
            'description' : 'Descrição',
            'start_estimated' : 'Data Abertura (estimado)',
            'end_estimated' : 'Data Conclusão (estimado)',
            'state': 'Estado',
            'leader': 'Responsável/Líder',
        }
        





        
