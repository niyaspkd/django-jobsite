from jobsite.models import Apply,Jobs
from django.forms import ModelForm
from django import forms

import re
from django import forms
from models import User
from django.utils.translation import ugettext_lazy as _

class SignupForm(forms.Form):
    ROLE_CHOICES    = [('1','Employer'), ('2','Employee')]
    username        = forms.CharField(required=True) 
    first_name      = forms.CharField(required=True) 
    last_name       = forms.CharField(required=True) 
    email 	        = forms.EmailField(required=True)
    password      = forms.CharField(widget=forms.PasswordInput(render_value=False))
    re_password     = forms.CharField(widget=forms.PasswordInput(render_value=False))
    role            = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect())


    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname','email','password','re_password')
        widgets = {
        'username': forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter username"}),
        'firstname': forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter firstname"}),
        'lastname': forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter lastname"}),
        'email': forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter email"}),
        'password': forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter password"}),
        're_password': forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter password again"}),

        }

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one."))

    def clean(self):
        if 'password' in self.cleaned_data and 're_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['re_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class UserDataForm(forms.ModelForm):
    class Meta:
     model = Apply
     fields = ['name', 'email', 'description', 'phone','job_id']
     widgets = {
			'name': forms.TextInput(attrs={"class":"form-control"}),
			
			'phone': forms.TextInput(attrs={"class":"form-control"}),
			'email': forms.EmailInput(attrs={"class":"form-control"}),
			'description': forms.Textarea(attrs={"class":"form-control"}),

            

            
            

			}


class JobDataForm(forms.ModelForm):
    class Meta:
     model = Jobs
     fields = ['title', 'description', 'location']
     widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            
            'date': forms.TextInput(attrs={"class":"form-control"}),
                      
            'location': forms.TextInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),

            

            
            

            }

			

	





