from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import User
from jobsite.models import Jobs,Apply


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','role',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'role', 'password','is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username','first_name','last_name','email', 'role', 'is_admin','is_active',)
    list_filter = ('is_admin', 'role',)
    fieldsets = (
        (None, {'fields': ('username','first_name','last_name','role','email', 'password',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','email','role', 'password1', 'password2',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)

admin.site.register(Jobs)

admin.site.register(Apply)