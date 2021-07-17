from django import forms
from .models import Info


class InfoForm(forms.Form):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        rpassword =forms.CharField(widget=forms.PasswordInput)
        model = Info
        fields = '_all_'
