from django import forms
from django.utils.translation import gettext_lazy as _


class loginForm(forms.Form):
    username = forms.CharField(label=_('username'), max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('username'), 'required': 'required'}))
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('password'), 'required': 'required'}))


class signupForm(forms.Form):
    username = forms.CharField(label=_('username'), max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('username'), 'required': 'required'}))
    email = forms.EmailField(label=_('email'), max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('email'), 'required': 'required'}))
    name = forms.CharField(label=_('name'), max_length=64, widget=forms.TextInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('name'), 'required': 'required'}))
    birth_date = forms.DateField(label=_('birth_date'), widget=forms.DateInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('birth date'), 'required': 'required'}))
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control rounded-0 border-0 my-4', 'placeholder': _('password'), 'required': 'required'}))
