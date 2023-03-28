from django import forms

class BoardForm(forms.Form):
    name = forms.CharField(max_length=30, label='name')
    email = forms.CharField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=8)