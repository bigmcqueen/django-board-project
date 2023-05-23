from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(),
            'content': forms.Textarea()
        }
