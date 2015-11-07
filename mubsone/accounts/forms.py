from django import forms

class LoginForm(forms.Form):
    username    = forms.CharField(label='username', max_length=256)
    password    = forms.CharField(label='password', max_length=256)

class RegisterForm(forms.Form):
    username    = forms.CharField(label='username', max_length=256)
    password    = forms.CharField(label='password', max_length=256)
    email       = forms.CharField(label='email', max_length=256)

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='old_password', max_length=256)
    new_password = forms.CharField(label='new_password', max_length=256)