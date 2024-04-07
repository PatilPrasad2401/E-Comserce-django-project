from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, \
    SetPasswordForm, PasswordResetForm
from django import forms
from django.contrib.auth.models import User

from .models import Customer,Complaint, Feedback


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirmpassword', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'password1', 'password2']


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='old Password', widget=forms.PasswordInput(
        attrs={'autofocus': 'true', 'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='new password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'state', 'address', 'city', 'zip_code']
        widgets = {
            'name': forms.TextInput(attrs={'class ': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class ': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class ': ' form-control'}),
        }


class Feedbackform(forms.ModelForm):
     class Meta:
         model = Feedback
         fields = [ 'description']
         widgets = {
             'desc': forms.TextInput(attrs={'class ': 'form-control'})
         }

class Complaintform(forms.ModelForm):
     class Meta:
         model = Complaint
         fields = [ 'description']
         widgets = {
             'desc': forms.TextInput(attrs={'class ': 'form-control'})
         }
