# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, ButtonHolder, Button, HTML
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Usuário:")
    password = forms.CharField(label="Senha:", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user-login'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(Div('username', css_class="col-4"), css_class="row"),
            Div(Div('password', css_class="col-4"), css_class="row"),
            Div(HTML("<br>"), css_class="row"),
            ButtonHolder(Submit('submit', 'Salvar', css_class='button white'), css_class='col-6')
            )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Password incorrect')
            if not user.is_active:
                raise forms.ValidationError('User disabled')

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Confirm email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')
        emails_qs = User.objects.filter(email=email)
        if emails_qs.exists():
            raise forms.ValidationError('Email already exists, please use other')
        return super(UserRegisterForm, self).clean(*args, **kwargs)

    # def clean_email2(self):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError('Emails must match')
    #     emails_qs = User.objects.filter(email=email)
    #     if emails_qs.exists():
    #         raise forms.ValidationError('Email already exists, please use other')
    #     return email
