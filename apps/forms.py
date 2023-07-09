from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChange(PasswordChangeForm):
    old_password =forms.CharField(
        label='Oldpassword',widget=forms.PasswordInput(attrs={'class':'form-control'}) )
    new_password1 = forms.CharField(
        label="New Password",widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    new_password2 = forms.CharField(
        label="Confirmpassword",widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
