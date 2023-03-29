from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), min_length=8, required=True)